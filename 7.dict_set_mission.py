## 1. 리스트 중복 제거
print('문제 1. 리스트 중복 제거')
l = [1,1,1,1,2,2,2,3,3,4,5,6,4,4,5,7,7,8,9,7,7,7,5,6,7]
print(l)

print('리스트를 세트 자료형으로 변경')
s = set(l)
print(s)

l = list(s)
print(l)

## 2. 튜플의 값을 추가, 수정, 삭제하기
print('\n문제 2. 튜플 값 변경')
t = (1,2,3,4,5,6,7,8)

l = list(t)
print(l)

l[0] = '값 변경'
print(l)

t = tuple(l)
print(t)


