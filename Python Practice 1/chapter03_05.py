# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

# 출력
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None 처리
print('b - ', b[1])
print('b - ', b.get(1))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'name' in a)
print('a - ', 'addr' in a)

# 수정
a['name'] = 'Seo'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)

temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)
