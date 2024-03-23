# 문자열 생성
str1 = "Hello Python"
str2 = 'Hello Python'
str3 = """Hello Python"""
str4 = '''Hello Python'''

print(str1, str2, str3, str4)
print(len(str1))

# 빈 문자열
str5 = ""
str6 = str()

print(type(str5), len(str5))
print(type(str6), len(str6))

# 이스케이프 문자 사용
"""
\n: 개행
\t: 탭
\\: 문자
\': 문자
\": 문자
\r: 캐리지 리턴
\f: 폼 피드
\a: 벨 소리
\b: 백 스페이스
\000: 널 문자
"""
print("I'm Boy")
print('I\'m Boy')

print('a \t b')
print('a \n b')

str7 = "Do you have a \"retro\" game?"
print(str7)

# 탭, 줄 바꿈
print("Click \t Start!")
print("New Line \n Check!")

# Raw String
print("C:\\Python\\test")
print(r"C:\Python\test")

# 멀티라인 입력
# 역슬래시 사용
multi_str = \
    """
문자열
멀티라인 입력
테스트
"""
print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(77), type(str(77)))
print(str(10.4), type(str(10.4)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("e"))
print("replace", str_o1.replace("thon", " Good"))
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' '))

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str))  # __iter__ 확인

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3])  # 0 1 2
print(str_s1[5:])  # 5부터 끝까지
print(str_s1[:len(str_s1)])  # 처음부터 끝까지
print(str_s1[:len(str_s1) - 1])  # 처음부터 끝까지 -1
print(str_s1[1:9:2])  # 1부터 9까지 2칸씩
print(str_s1[-5:])  # 뒤에서 5번째부터 끝까지
print(str_s1[1:-2])  # 뒤에서 2번째까지
print(str_s1[::2])  # 처음부터 끝까지 2칸씩
print(str_s1[::-1])  # 처음부터 끝까지 역순

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a))  # 아스키 코드로 변환
print(chr(122))  # 문자로 변환
