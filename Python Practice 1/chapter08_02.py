# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류: sys, pickle, shutil, temfile, time, random 등

# sys: 파이썬 인터프리터 제어
import sys
print(sys.argv)  # 파일 실행 시 전달되는 인자 확인

# 강제 종료
# sys.exit()

# 파이썬 패키지 위치
print(sys.path)

# pickle: 객체 파일 읽기, 쓰기
import pickle

# 쓰기
f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

# 읽기
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data)
f.close()

# os: 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업
# mkdir, rmdir(비어있으면 삭제), rename

import os

# 시스템 정보
print(os.environ)

# 현재 경로
print(os.getcwd())

# time : 시간 관련 처리
import time

# 현재 시간
print(time.time())

# 형태 변환
print(time.localtime(time.time()))

# 간단 표현
print(time.ctime())

# 형식 표현
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 시간 간격 발생
for i in range(5):
    print(i)
    time.sleep(1)

# random: 난수 생성
import random

# random.random(): 0 ~ 1 사이 실수
print(random.random())

# random.randint(1, 10): 1 ~ 10 사이 정수
print(random.randint(1, 10))

# shuffle: 리스트의 항목 섞기
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 리스트에서 1개 선택
print(random.choice([1, 2, 3, 4, 5]))

# webbrowser: 본인 OS의 웹 브라우저 실행
import webbrowser

webbrowser.open('http://google.com')
webbrowser.open_new('http://google.com')
webbrowser.open_new_tab('http://google.com')
