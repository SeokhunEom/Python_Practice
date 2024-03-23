# 숫자형

# 파이썬 지원 자료형
"""
int: 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
"""

# 데이터 타입
str1 = "Python"
bool1 = True
str2 = 'Anaconda'
float1 = 10.0  # 10 == 10.0
int1 = 7
list1 = [str1, str2]
dict1 = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple1 = (7, 8, 9)
set1 = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool1))
print(type(float1))
print(type(int1))
print(type(list1))
print(type(dict1))
print(type(tuple1))
print(type(set1))

# 숫자형 연산자
"""
+: 덧셈
-: 뺄셈
*: 곱셈
/: 나눗셈
//: 몫
%: 나머지
abs(x): 절대값
pow(x, y), x ** y: x의 y제곱
"""

# 정수 선언
i1 = 77
i2 = -14
i3 = 9999999999999999999999999999999999999999

# 정수 출력
print(i1)
print(i2)
print(i3)

# 실수 선언
f1 = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

# 실수 출력
print(f1)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
i3 = 9999999999999999999999999999999999999999
i4 = 8888888888888888888888888888888888888888
f1 = 39.222
f2 = 939.393

# +
print(">>>>>+")
print("i1 + i2:", i1 + i2)
print("i3 + i4:", i3 + i4)
print("f1 + f2:", f1 + f2)

# *
print(">>>>>*")
print("i1 * i2:", i1 * i2)
print("i3 * i4:", i3 * i4)
print("f1 * f2:", f1 * f2)

# -
print(">>>>>-")
print("i1 - i2:", i1 - i2)
print("i3 - i4:", i3 - i4)
print("f1 - f2:", f1 - f2)

# /
print(">>>>>/")
print("i2 / i1:", i2 / i1)
print("i3 / i4:", i3 / i4)
print("f2 / f1:", f2 / f1)

# //
print(">>>>>//")
print("i2 // i1:", i2 // i1)
print("i3 // i4:", i3 // i4)

# %
print(">>>>>%")
print("i1 % i2:", i1 % i2)
print("i3 % i4:", i3 % i4)

# 형 변환 실습
a = 5.
b = 4
c = .4
d = 7.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))  # True: 1, False: 0
print(float(False))
print(complex(3))
print(complex('3'))  # 문자형 -> 숫자형
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3), 5 ** 3)

# 외부 모듈
import math

print(math.ceil(5.1))  # x 이상의 수 중에서 가장 작은 정수
print(math.pi)
