# 파이썬 사용자 입력
# Input 사용법
# 기본 타임(str)

# 예제1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company Name : ")

print(name, grade, company)

# 예제2
number = input("Enter Number : ")
name = input("Enter Name : ")

print("Type of Number", type(number))
print("Type of Name", type(name))

# 예제3(계산)
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))
total = first_number + second_number
print("Total :", total)

# 예제4
float_number = float(input("Enter a float number : "))
print("input float :", float_number)
print("input type :", type(float_number))

# 예제5
print("FirstName - {0}, LastName - {1}".format(input("Enter First Name : "), input("Enter Last Name : ")))

# 예외 처리
# 예제 1
try:
    n = int(input("Enter a number : "))
    print("Your number is :", n)
except ValueError:
    print("This is not a number")

# 예제 2
while True:
    try:
        n = int(input("Enter a number : "))
        print("Your number is :", n)
        break
    except ValueError:
        print("This is not a number")
