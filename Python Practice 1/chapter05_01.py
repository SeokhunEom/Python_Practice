# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#   code

# 예제1
def first_func(w):
    print("Hello,", w)


word = "Goodboy"
first_func(word)


# 예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value


x = return_func('Goodboy2')
print(x)


# 예제3(다중반환)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


q = func_mul(100)
print(type(q), q)

x, y, z = func_mul(100)
print(type(x), x, y, z)


# 리스트 리턴
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


p = func_mul2(100)
print(type(p), p)


# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}


d = func_mul3(100)
print(type(d), d)
print(d.get('ret1'), d.get('ret2'), d.get('ret3'))
print(d.items())
print(d.keys())
print(d.values())


# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')


# **kwargs(언팩킹)
def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-----')


kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
example_mul(10, 20, 'Lee', 'Kim', 'Park')
example_mul(10, 20, 'Lee', 'Kim', 'Park', age1=33, age2=34, age3=44)


# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)


nested_func(100)


# 실행불가
# func_in_func(200)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 남발시 가독성 오히려 감소

def mul_func(x, y):
    return x * y


lambda_mul_func = lambda x, y: x * y

print(mul_func(10, 50))
print(lambda_mul_func(10, 50))


# 함수를 매개변수로 넘겨줄 때 람다식을 사용하면 편리하다.
def func_final(x, y, func):
    print(x * y * func(10, 50))


func_final(10, 20, lambda x, y: x * y)
