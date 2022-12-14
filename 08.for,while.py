##################################################
##               [8] 파이썬 반복문               ##
##################################################

# print("\n" + "1.1. for 반복문")
for i in [1, 2, 3, 4]:
    print(i)

# print("\n" + "1.2. while 반복문")
a = 5
while a>0:
    print(a)
    a -= 1

# print("\n" + "1.3. range 함수 활용")
print([i for i in range(5)])

# print("\n" + "1.4. range 함수 고급")
print([i for i in range(5) if i%2 == 0])


##################################################
##           Mission 1. 반복문 활용              ##
##################################################

# print("\n" + "2.1. 구구단")
num = int(input("출력할 단 수를 입력해주세요 : "))

for i in range(1, 10):
    print("{} X {} = {}".format(num, i, num*i))


##################################################
##        Mission 2. 리스트 내포 활용            ##
##################################################

# print("\n" + "3.1. 구구단을 2~9단 출력하는 코드, 4단은 건너뛰기")
l = []
for i in range(2,10):
    for j in range(1,10):
        if(i != 4):
            l.append(i*j)
print(l)

print([i*j for i in range(2,10) for j in range(1,10) if i !=4])
