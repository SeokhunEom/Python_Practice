"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('010', '1234', '5678', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용(d, s, f)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % 'nice')
print('{:>10}'.format('nice'))

print('%-10s' % 'nice')
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % 'nice')
print('%.5s' % 'pythonstudy')
print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % 42)
print('{:4d}'.format(42))

print()

# %f
print('%f' % 3.141592653589793)
print('{:f}'.format(3.141592653589793))
print('%06.2f' % 3.141592653589793)
print('{:06.2f}'.format(3.141592653589793))

print()

# 3가지 Format 연습
x = 50
y = 100
text = 12345678
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, x + y)
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x + y)
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

print()

# 구분기호
m = 100000000
print(f'm: {m:,}')

print()

# 정렬
# ^: 가운데, <: 왼쪽, >: 오른쪽
t = 20

print(f't: {t:10}')
print(f't: {t:^10}')
print(f't: {t:<10}')
print(f't: {t:>10}')
print(f't: {t:#^10}')

print()
