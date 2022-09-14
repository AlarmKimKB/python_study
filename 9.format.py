s = "안녕하세요. 학습자님!"
print(s.split('.'))

s = "ABCDefGHJ"
print(s.lower())


## 문자열 포맷팅

a = "{}, World!".format("Hello!")
print(a)

a = "{} {} {}".format("Hello",",","World!")
print(a)

a = "{}, {}, {}, {}".format("2",2,(1,2),[1,2])
print(a)

### Formating Example
print("{} 더하기 {} 는 {}".format(1,2,3))

print("{1} 더하기 {0} 는 {2}".format(1,2,3))


### Mission 1. 문자열의 특징, 메소드 등을 활용하여 특정 문자 뽑아내기
## S에서 31을 뽑아 출력
print("문제 1")

s = "Today is December 31, 2020. Tomorrow is January 1, 2021."
print(s)

# a = s.split()
# print(a[3])

temp = s.split(',')[0]
print(temp)
print(temp.split(' '))

result = temp.split()[3]
print(result)

# print(s[5:8])

### Mission 2. 문자열 포맷팅 활용
print("문제 2")

print("{} X {:f} = {}".format(2,2,4))
print("{} X {} = {:2}".format(2,3,6))
print("{} X {} = {}".format(2,4,8))
print("{} X {} = {}".format([2],5,10))
print("{} X {} = {}".format(2,6,12))
print("{} X {} = {}".format(2,7,"십사"))
print("{} X {} = {}".format(2,8,16))
print("{} X {:0.1f} = {:2f}".format(2,9,18))
