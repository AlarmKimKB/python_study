# for 반복문

for i in [1, 2, 3, 4]:
    print(i)


# while 반복문
a = 5
while a>0:
    print(a)
    a -= 1

print([i for i in range(5)])

print([i for i in range(5) if i%2 == 0])

## Mission 1. 반복문 활용
# 구구단
# num = int(input("출력할 단 수를 입력해주세요 : "))

# for i in range(1, 10):
#     print("{} X {} = {}".format(num, i, num*i))

## Mission 2. 리스트 내포 활용
# 구구단을 2단부터 9단까지 출력하는 코드 작성, 4단은 건너뛰기

l = []
for i in range(2,10):
    for j in range(1,10):
        if(i != 4):
            l.append(i*j)
print(l)

print([i*j for i in range(2,10) for j in range(1,10) if i !=4])
