#
#  Copyright 2023 The FATE Authors. All Rights Reserved.
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

from typing import Union, Mapping

from fate.arch import Context
from fate.components.core import GUEST, HOST, Role, cpn, params
from fate.ml.model_selection.sample import SampleModuleGuest, SampleModuleHost


@cpn.component(roles=[GUEST, HOST], provider="fate")
def sample(
        ctx: Context,
        role: Role,
        input_data: cpn.dataframe_input(roles=[GUEST, HOST]),
        mode: cpn.parameter(type=params.string_choice(['random', 'stratified', 'weight']),
                            default='random',
                            desc="sample mode, if select 'weight', "
                                 "will use dataframe's weight as sampling weight, default 'random'"),
        replace: cpn.parameter(type=bool, default=False,
                               desc="whether allow sampling with replacement, default False"),
        frac: cpn.parameter(type=Union[params.confloat(gt=0.0),
        Mapping[Union[params.conint(), params.confloat()], params.confloat(gt=0.0)]],
                            default=None, optional=True,
                            desc="if mode equals to random, it should be a float number greater than 0,"
                                 "otherwise a dict of pairs like [label_i, sample_rate_i],"
                                 "e.g. {0: 0.5, 1: 0.8, 2: 0.3}, any label unspecified in dict will not be sampled,"
                                 "default: 1.0, cannot be used with n"),
        n: cpn.parameter(type=Union[params.conint(gt=0),
        Mapping[Union[params.conint(), params.confloat()], params.conint(gt=0)]], default=None, optional=True,
                         desc="exact sample size, it should be an int greater than 0, "
                              "otherwise a dict of pairs like [label_i, sample_count_i],"
                              "e.g. {0: 50, 1: 20, 2: 30}, any label unspecified in dict will not be sampled,"
                              "default: None, cannot be used with frac"),
        random_state: cpn.parameter(type=params.conint(ge=0), default=None,
                                    desc="random state"),
        ctx_mode: cpn.parameter(type=params.string_choice(["hetero", "homo", "local"]), default="hetero",
                                desc="sampling mode, 'homo' & 'local' will both sample locally"),
        output_data: cpn.dataframe_output(roles=[GUEST, HOST])
):
    if frac is not None and n is not None:
        raise ValueError(f"n and frac cannot be used at the same time")
    if mode in ["random"] and (isinstance(frac, dict) or isinstance(n, dict)):
        raise ValueError(f"frac or n must be single value when mode set to {mode}")
    if frac is not None and frac > 1 and not replace:
        raise ValueError(f"replace has to be set to True when sampling frac greater than 1.")
    if n is None and frac is None:
        frac = 1.0

    sub_ctx = ctx.sub_ctx("train")
    if role.is_guest:
        module = SampleModuleGuest(mode=mode, replace=replace, frac=frac, n=n,
                                   random_state=random_state, ctx_mode=ctx_mode)
    elif role.is_host:
        module = SampleModuleHost(mode=mode, replace=replace, frac=frac, n=n,
                                  random_state=random_state, ctx_mode=ctx_mode)
    else:
        raise ValueError(f"unknown role")
    input_data = input_data.read()

    sampled_data = module.fit(sub_ctx, input_data)

    output_data.write(sampled_data)