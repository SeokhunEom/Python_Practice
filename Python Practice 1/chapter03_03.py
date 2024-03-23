# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서 o, 중복 o, 수정 o, 삭제 o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)  # d의 타입과 값
print('d - ', d[1])  # d의 1번째 인덱스
print('d - ', d[0] + d[1] + d[1])  # 1000 + 10000 + 10000
print('d - ', d[-1])  # 맨 뒤에서 첫번째
print('e - ', e[-1][1])  # e 리스트 안에 있는 리스트의 1번째 인덱스
print('e - ', list(e[-1][1]))  # e 리스트 안에 있는 리스트의 1번째 인덱스를 리스트로 변환

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])  # 0 ~ 3까지
print('d - ', d[2:])  # 2부터 끝까지
print('e - ', e[-1][1:3])  # e 리스트 안에 있는 리스트의 1 ~ 3까지

# 리스트 연산
print('>>>>>')
print('c + d', c + d)  # c와 d를 합침
print('c * 3', c * 3)  # c를 3번 반복
print("'Test' + c[0]", 'Test' + str(c[0]))  # c의 0번째 인덱스를 문자열로 변환하여 합침

# 값 비교
print('>>>>>')
print(c == c[:3] + c[3:])  # c와 c의 0 ~ 3까지와 3부터 끝까지 비교
print(c)
print(c[:3] + c[3:])

# Identity(id)
print('>>>>>')
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2]
print('c - ', c)

# 리스트 함수
print('>>>>>')
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(6)  # 리스트에 6 추가
print('a - ', a)
a.sort()  # 리스트 정렬
print('a - ', a)
a.reverse()  # 리스트 역순
print('a - ', a)
print('a - ', a.index(3), a[3])  # 3의 인덱스와 값
a.insert(2, 7)  # 2번째 인덱스에 7 추가
print('a - ', a)
a.reverse()  # 리스트 역순
print('a - ', a)
a.remove(6)  # 10 삭제
print('a - ', a)
print('a - ', a.pop())  # 마지막 인덱스 값 출력 후 삭제
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))  # 4의 개수
ex = [8, 9]
a.extend(ex)  # 리스트에 ex 리스트 추가
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
