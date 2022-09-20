##################################################
##               [9] 파이썬 입출력               ##
##################################################

# print("\n" + "1.1. 파일 쓰기")
f = open("a.txt", 'w')
f.write('1234')
f.close()

# print("\n" + "1.2. 파일 쓰기, 리스트 & 튜플")
t = ("1","2","3","4")
f = open("a.txt", "w")
f.writelines(t)
f.close()

# print("\n" + "1.3. 다른 자료형의 파일 입출력")
import pickle
f = open("a.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()


##################################################
##       Mission 1. 표준 출력을 파일로 변경       ##
##################################################

# print("\n" + "2.1. 구구단을 파일에 저장")
from os import getcwd       # 현재 위치 확인
print(getcwd())

import sys
f = open('b.txt', 'w')
sys.stdout = f              # sys 모듈의 표준 출력을 f 파일에 저장

for i in range(2,10):       # 해당 for문에 대한 출력은 f 파일에 저장됨
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))



##################################################
##       Mission 2. 폴더 생성 후 파일에 저장      ##
##################################################

# print("\n" + "3.1. python 폴더 생성 후, 파일 생성")
"""
안녕하세요. 학습자님!
이번 회자에서는
파이썬의 파일 입출력에 대해서
학습했습니다.
"""
txt = "Hello, World"

import os
os.getcwd()         # 현재 위치 확인
os.mkdir('c:\\Users\\MZC01-SCOTTKIM\\Desktop\\python')
f = open('c:\\Users\\MZC01-SCOTTKIM\\Desktop\\python\\text.txt', 'w')
f.write(txt)
f.close()

# print("\n" + "3.2. 현재 위치를 변경 후 출력")
os.chdir('c:\\Users\\MZC01-SCOTTKIM\\Desktop\\python')      # 현재 위치 변경
print(os.getcwd())
f = open('test.txt', 'w')
f.write(txt)
f.close()
