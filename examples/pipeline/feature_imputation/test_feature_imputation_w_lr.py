#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import argparse

from fate_client.pipeline import FateFlowPipeline
from fate_client.pipeline.components.fate import CoordinatedLR, PSI, HeteroFeatureBinning, FeatureImputation
from fate_client.pipeline.interface import DataWarehouseChannel
from fate_client.pipeline.utils import test_utils


def main(config="../config.yaml", namespace=""):
    if isinstance(config, str):
        config = test_utils.load_job_config(config)
    parties = config.parties
    guest = parties.guest[0]
    host = parties.host[0]
    arbiter = parties.arbiter[0]

    pipeline = FateFlowPipeline().set_roles(guest=guest, host=host, arbiter=arbiter)
    if config.task_cores:
        pipeline.conf.set("task_cores", config.task_cores)
    if config.timeout:
        pipeline.conf.set("timeout", config.timeout)

    psi_0 = PSI("psi_0")
    psi_0.guest.component_setting(input_data=DataWarehouseChannel(name="breast_hetero_guest",
                                                                  namespace=f"experiment{namespace}"))
    psi_0.hosts[0].component_setting(input_data=DataWarehouseChannel(name="breast_hetero_host",
                                                                     namespace=f"experiment{namespace}"))

    psi_1 = PSI("psi_1")
    psi_1.guest.component_setting(input_data=DataWarehouseChannel(name="breast_hetero_guest",
                                                                  namespace=f"experiment{namespace}"))
    psi_1.hosts[0].component_setting(input_data=DataWarehouseChannel(name="breast_hetero_host",
                                                                     namespace=f"experiment{namespace}"))

    binning_0 = HeteroFeatureBinning("binning_0",
                                     method="bucket",
                                     n_bins=5,
                                     bin_col=["x0", "x3"],
                                     transform_method="bin_idx",
                                     train_data=psi_0.outputs["output_data"])
    feature_imputation_0 = FeatureImputation("feature_imputation_0",
                                             method="consts",
                                             fill_const=10,
                                             # missing_val=[0],
                                             train_data=binning_0.outputs["train_output_data"])

    lr_0 = CoordinatedLR("lr_0",
                         epochs=10,
                         batch_size=None,
                         optimizer={"method": "SGD", "optimizer_params": {"lr": 0.21}},
                         init_param={"fit_intercept": True, "method": "random_uniform"},
                         train_data=feature_imputation_0.outputs["train_output_data"],
                         learning_rate_scheduler={"method": "linear", "scheduler_params": {"start_factor": 0.7,
                                                                                           "total_iters": 100}})

    pipeline.add_task(psi_0)
    pipeline.add_task(psi_1)
    pipeline.add_task(binning_0)
    pipeline.add_task(feature_imputation_0)
    pipeline.add_task(lr_0)

    # pipeline.add_task(hetero_feature_binning_0)
    pipeline.compile()
    print(pipeline.get_dag())
    pipeline.fit()

    pipeline.deploy([psi_0, binning_0, feature_imputation_0, lr_0])

    predict_pipeline = FateFlowPipeline()

    deployed_pipeline = pipeline.get_deployed_pipeline()
    deployed_pipeline.psi_0.guest.component_setting(input_data=DataWarehouseChannel(name="breast_hetero_guest",
                                                                                    namespace=f"experiment{namespace}"))
    deployed_pipeline.psi_0.hosts[0].component_setting(input_data=DataWarehouseChannel(name="breast_hetero_host",
                                                                                       namespace=f"experiment{namespace}"))

    predict_pipeline.add_task(deployed_pipeline)
    predict_pipeline.compile()
    # print("\n\n\n")
    # print(predict_pipeline.compile().get_dag())
    predict_pipeline.predict()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("PIPELINE DEMO")
    parser.add_argument("--config", type=str, default="../config.yaml",
                        help="config file")
    parser.add_argument("--namespace", type=str, default="",
                        help="namespace for data stored in FATE")
    args = parser.parse_args()
    main(config=args.config, namespace=args.namespace)