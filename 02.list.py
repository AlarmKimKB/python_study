##################################################
##              [2] 파이썬 리스트                ##
##################################################

# print("\n" + "1.1. 리스트 선언")
l = []          # 대괄호로 선언 []
l2 = list()     # list 함수로 선언

print(type(l))
print(type(l2))

# print("\n" + "1.2. 리스트 인덱스 값 유형")
l = [1, "문자", [1,2,3], (1,2,3)]   # 정수(int), 문자열(string), 리스트(list), 튜플(tuple) 등 가능
print(l)


##################################################
##              2. 리스트 인덱싱                 ##
##################################################

# print("\n" + "2.1. 리스트 인덱싱")
print(l[0])         # 1번째 인덱스 값 출력 (1)
print(l[1])         # 2번째 인덱스 값 출력 ("문자")

print(type(l[1]))   # 2번째 인덱스 값 type 출력 (string)

print(l[0:4])       # 1번째 부터 3번째 인덱스 값 출력
print(l[0:2])       # 1번째 부터 1번째 인덱스 값 출력


# print("\n" + "2.2. 인덱스 추가")
l.append(4)         # 마지막에 4 값 추가
print(l)


##################################################
##           Mission 1. 리스트 정렬              ##
##################################################
l = [2,5,1,3,6,4,8,7,9]
print(l)

# print("\n" + "3.1. sorted 내장 함수 사용")
print(sorted(l))

l.sort()
print(l)

# print("\n" + "3.2. 내림차순 정렬")
l.sort(reverse=True)
print(l)

l = [2,5,1,3,6,4,8,7,9]
print(l)

l.sort()
l.reverse()
print(l)

