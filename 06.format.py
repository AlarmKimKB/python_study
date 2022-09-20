##################################################
##              [6] 파이썬 포맷팅                ##
##################################################

# print("\n" + "1.1. 문자열 나누기")
s = "안녕하세요. 학습자님!"
print(s.split('.'))     # .을 구분자로 구분

# print("\n" + "1.2. 문자열 변환")
s = "ABCDefGHJ"
print(s.lower())        # 소문자로 변환


##################################################
##               2. 문자열 포맷팅                ##
##################################################

# print("\n" + "2.1. 포맷팅")
a = "{}, World!".format("Hello!")
print(a)

a = "{} {} {}".format("Hello",",","World!")
print(a)

a = "{}, {}, {}, {}".format("2",2,(1,2),[1,2])      # {}값에 정수(int), 문자열(string), 리스트(list), 튜플(tuple) 등 가능
print(a)

print("{} 더하기 {} 는 {}".format(1,2,3))

# print("\n" + "2.2. 포맷팅 고급")
print("{1} 더하기 {0} 는 {2}".format(1,2,3))        # {} 안에 인덱스 위치 지정 가능


##################################################
##         Mission 1. 문자열 포맷팅              ##
##################################################

# print("\n" + "3.1. 특정 문자 뽑아내기")
s = "Today is December 31, 2020. Tomorrow is January 1, 2021."   # S에서 31을 뽑아 출력
print(s)

temp = s.split(',')[0]              # ,를 구분자로 구분한 리스트 요소 중, 첫 번째 값을 temp 변수에 저장
print("temp = " + temp)
print(temp.split(' '))              # 공백을 구분자로 구분

result = temp.split()[3]            # 공백을 구분자로 구분한 리스트 요소 중, 두 번째 값을 result 변수에 저장
print("temp.split()[3] = " + result)


##################################################
##       Mission 2. 문자열 포맷팅 활용           ##
##################################################

# print("\n" + "4.1. 문자열 포맷팅 활용")
print("{} X {:f} = {}".format(2,2,4))         # {:f} 로 실수값으로 변경
print("{} X {} = {:2}".format(2,3,6))         # {:2} 숫자를 통해 공백 출력 가능
print("{} X {} = {}".format(2,4,8))           
print("{} X {} = {}".format([2],5,10))        # {} 안에 리스트 값 가능
print("{} X {} = {}".format(2,6,12))
print("{} X {} = {}".format(2,7,"십사"))
print("{} X {} = {}".format(2,8,16))
print("{} X {:0.1f} = {:2f}".format(2,9,18))  # {:0.1f} 를 통해 소수점 첫 번째까지 자리 수 변경
