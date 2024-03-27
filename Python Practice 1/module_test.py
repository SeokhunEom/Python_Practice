# 모듈 사용 실습

import sys
import time

print(sys)
print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('C:/Python/Python3/06/module_test')

import test_module

print(test_module.power(10, 3))