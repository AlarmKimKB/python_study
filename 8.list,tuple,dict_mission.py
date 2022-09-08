# 1. 리스트 함수 활용, 값 정렬
l = [2,5,1,3,6,4,8,7,9]
print(l)

# 방법 1. sorted 내장 함수 사용
print(sorted(l))

# 방법 2. list 함수 사용
l.sort()
print(l)

# 내림차순 정렬
l.sort(reverse=True)
print(l)

# 방법 3. reverse 함수 사용
l = [2,5,1,3,6,4,8,7,9]
print(l)

l.sort()
l.reverse()
print(l)


## 2. 두 사전을 하나의 사전으로 병합
dic1 = {'a' : 1 , 'b' : 2 , 'c' : 3}
dic2 = {'b' : 5 , 'c' : 1 , 'd' : 7}

# 실행결과 = {'a' : 1 , 'b' : 5 , 'c' : 1 , 'd' : 7}

dic1.update(dic2)
print(dic1)
