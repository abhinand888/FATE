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
#
from pyspark import SparkContext
sc = SparkContext('local', 'test')
sc.parallelize()
#logFile = "file:///Users/jingwang/Documents/tools/spark-2.1.1-bin-hadoop2.7/README.md"
#logData = sc.textFile(logFile, 2).cache()
#numAs = logData.filter(lambda line: 'a' in line).count()
#numBs = logData.filter(lambda line: 'b' in line).count()
#print('Lines with a: %s, Lines with b: %s' % (numAs, numBs))