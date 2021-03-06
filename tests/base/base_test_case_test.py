# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import os.path
import sys
import __main__

from citest.base import BaseTestCase
from citest.base import TestRunner


tested_main = False

class BaseTestCaseTest(BaseTestCase):
  def test_logging(self):
    self.log_start_test()
    self.log_end_test(name='Test')


if __name__ == '__main__':
  result = TestRunner.main(test_case_list=[BaseTestCaseTest])
  if not tested_main:
     raise Exception("Test Failed.")

  sys.exit(result)
