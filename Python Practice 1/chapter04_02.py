# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

for v1 in range(10):  # 0 ~ 9
    print('v1 is :', v1)

print()

for v2 in range(1, 11):  # 1 ~ 10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):  # 1 ~ 10 까지 2씩 증가
    print('v3 is :', v3)

print()

# 1 ~ 1000 합
sum1 = 0
for v in range(1, 1001):
    sum1 += v
print('1 ~ 1000 Sum :', sum1)
print('1 ~ 1000 Sum :', sum(range(1, 1001)))  # sum 함수 사용
print('1 ~ 1000 4의 배수의 합 :', sum(range(4, 1001, 4)))

print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('You are :', name)
print()

lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
    print("Current number :", n)
print()

word = "Beautiful"
for s in word:
    print('Word :', s)
print()

my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}
for key in my_info:
    print('key :', key)
for v in my_info.values():
    print('value :', v)
print()

name = 'FineAppLE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not found :', num)
print()

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print("current type:", v, type(v))
print()

# for - else 구문
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 49:
        print("Found : 49!")
        break
else:
    print("Not Found 49....")

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()
print()

# 변환 예제
name = 'Aceman'
print('Reversed :', reversed(name))
print('List :', list(reversed(name)))
print('Tuple :', tuple(reversed(name)))
print('Set :', set(reversed(name)))  # 순서X
