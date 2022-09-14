## Mission 1. 표준 출력을 파일로 변경하여 구구단을 파일에 저장
# print()로 출력
# 문자열 포맷팅 활용
# 반복문 활용, 2-9 단 출력

# from os import getcwd
# print(getcwd())

# import sys
# f = open('b.txt', 'w')
# sys.stdout = f

# for i in range(2,10):
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j))


## Mission 2. 바탕화면에 python 폴더 생성 후, 파일 생성
"""
안녕하세요. 학습자님!
이번 회자에서는
파이썬의 파일 입출력에 대해서
학습했습니다.
"""
txt = "Hello, World"

import os

os.getcwd()
# os.mkdir('c:\\Users\\MZC01-SCOTTKIM\\Desktop\\python')
# f = open('c:\\Users\\MZC01-SCOTTKIM\\Desktop\\python\\text.txt', 'w')
# f.write(txt)
# f.close()

os.chdir('c:\\Users\\MZC01-SCOTTKIM\\Desktop\\python')
print(os.getcwd())
f = open('test.txt', 'w')
f.write(txt)
f.close()



