##################################################
##             [11] 파이썬 람다 함수             ##
##################################################

# print("\n" + "1.1. map 함수 예제")
def func(x):
    return x * x

a = [1, 2, 3, 4, 5]
b = map(func, a)        # func 에 a 값 반복 대입하여 값 출력 -> map type으로 반환

print(type(b))
print(list(b))

# print("\n" + "1.2. map 함수 lambda 활용")
print(list(map(lambda x : x*x, [1, 2, 3, 4, 5])))

# print("\n" + "1.3. filter 함수 예제")
def func(x):
    return x > 2

a = [1, 2, 3, 34]
b = []

print(list(filter(func, a)))    # func 에 a 값 반복 대입하여 true인 값 출력 -> 해당 값 list type으로 반환

# print("\n" + "1.4. filter 함수 lambda 활용")
print(list(filter(lambda x : x > 2 , [1, 2, 3, 34])))


# print("\n" + "1.5. 복잡한 객체 정렬")
student = [
    ('영수', 'A', 15),
    ('철수', 'B', 16),
    ('영희', 'C', 10)
]

print(sorted(student))                          # 첫 번째 요소에 대한 값들로만 정렬 ex. 영수, 철수
print(sorted(student, key=lambda x : x[1]))     # 두 번째 요소에 대한 값들로만 정렬 ex. A, B, c
print(sorted(student, key=lambda x : x[2]))     # 세 번째 요소에 대한 값들로만 정렬 ex. 15, 16, 10

# print("\n" + "1.6. 문자열 포맷팅 활용")
print((lambda x, y : '{} X {} = {}'.format(x, y, x*y))(3, 4))


##################################################
##                 2. 재귀 함수                  ##
##################################################

# print("\n" + "2.1. 팩토리얼")
def factorial(n):
    if n == 0 :     # 종료 조건 작성
        return 1    # n = 0 일 경우, 1 반환
    return n * factorial(n-1)

print(factorial(5))

# print("\n" + "2.2. 팩토리얼 lambda 활용")
fact = lambda x : x == 0 and 1 or x * fact(x-1)
print(fact(5))

# print("\n" + "2.3. 구구단 출력")
l = []
for i in range(2, 10):
    for j in range(1, 10):
        l.append("{} x {} = {}".format(i, j, i*j))

print(l)

# print("\n" + "2.4. 리스트 내포 활용")
print([x * y for x in range(2, 10) for y in range(1, 10)])

# print("\n" + "2.5. 구구단 lambda 활용")
print((lambda x, y : '{} x {} = {}'.format(x, y, x*y))(3, 4))

# print("\n" + "2.6. 구구단 리스트 내포, lambda 활용")
print([(lambda x, y : '{} x {} = {}'.format(x, y, x*y))(x, y) for x in range(2, 10) for y in range(1, 10)])


##################################################
##         Mission 1. 람다 함수 변경             ##
##################################################

def func(a):
    if a >10 :
        return 'a가 10보다 크다'
    else:
        return 'a가 10보다 작다'
print(func(14))

print((lambda a : 'a가 10보다 크다' if a > 10 else 'a가 10보다 작다')(14))


##################################################
##        Mission 2. map, 람다 함수 활용         ##
##################################################

def func(a) :
    l = []
    for i in range(a):
        l.append(i**2)
    return l
print(func(5))

print(list(map((lambda a : a**2),range(5))))

