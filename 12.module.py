
##################################################
##         Mission 1. random 모듈 활용           ##
##################################################

# print("\n" + "2.1. 1~45 사이 랜덤 6개 출력")
# import random

# for i in range(6):
#     print(random.randint(1, 45))

# print("\n" + "2.2. 로또 번호 생성기 만들기")
# l = []
# while True:
#     temp = random.randint(1, 45)
#     if temp not in l:
#         l.append(temp)
#     if len(l) == 6:
#         break
# print(l)

# l = []
# while True:
#     l.append(random.randint(1, 45))
#     l = set(l)
#     l = list(l)
#     if len(l) == 6:
#         break
# print(l)


##################################################
##              2. 외부 모듈 사용                ##
##################################################

# print("\n" + "3.1. pip 설치")
# pip install pymysql       # 콘솔창에 해당 명령어 입력, python과 mysql 연결
# pip install beautifulsoap4

import pymysql

dbURL = "mysql.cyhucz1bf0kf.ap-northeast-2.rds.amazonaws.com"
dbPort = 3306
dbUser = "sysadm"
dbPass = "sysadmin123!"

conn = pymysql.connect (
    host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='test', use_unicode=True
)

sql = "select * from test.test"

print(conn)

cur =conn.cursor()
cur.execute(sql)
result = cur.fetchall()
conn.commit()


##################################################
##      Mission 2. BeautifulSoup 모듈 활용       ##
##################################################

# print("\n" + "4.1. 급상승 검색어 가져오는 웹 크롤링 코드")
# pip install beautifulsoap4  / bs4

# import bs4
# import urllib.request as urllib

# url = "https://www.naver.com"
# web_page = urllib.urlopen(url)

# # print(web_page.read())

# html_text = bs4.BeautifulSoup(web_page, "html.parser")
# # print(html_text)

# a = html_text.find('li', class_='')
