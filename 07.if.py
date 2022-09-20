##################################################
##             [7] 파이썬 if 조건문              ##
##################################################

# print("\n" + "1.1. if 문")
a = 4
if a > 3:
    print(1)

# print("\n" + "1.2. if/elif/else 문")
a = 4
if a == 1 :
    print(1)
elif a == 2:
    print(2)
else:
    print(4)

# print("\n" + "1.3. 조건문 표현식")
a = 1
msg2 = "a is 1" if (a == 1) else "a is not 1"
print(msg2)


##################################################
##            Mission 1. 조건문 활용             ##
##################################################

# print("\n" + "2.1. 조건문 활용")
a = int(input("키를 입력해주세요 : "))
b = int(input("몸무게를 입력해주세요 : "))

if a > 180:
    print("남자")
elif a < 160:
    print("여자")
elif (160<= a <= 180):
    if (b >= (a-110)):
        print("남자")
    else:
        print("여자")
else:
    print("모르겠습니다.")

# print("\n" + "2.2. 조건문 활용")
a = 1
if (a > 0):
    msg = 'a는 양수입니다.'
else:
    msg = 'a는 음수입니다.'

if (a == 0):
    msg2 = 'a는 0입니다.'
else:
    msg2 = 'a는 0이 아닙니다.'

print(msg, msg2)

# print("\n" + "2.3. 조건문 표현식 활용")
msg = 'a는 양수입니다' if a > 0 else 'a는 음수입니다.'
print(msg)

msg2 = 'a는 0입니다.' if a==0 else 'a는 0이 아닙니다.'
print(msg2)
