d = {}
d2 = dict()
print(type(d))
print(type(d2))

d = {
    'a' : 1,
    'b' : 2
}
print(d)

# 변경 불가능한 객체가 와야되기 때문에 변경 가능한 리스트는 키 값 불가
# d = {
#     [1,2] : 1
# }
# print(d)

# 변경 불가능한 객체인 튜플은 키 값 가능
d = {
    (1,2) : 1
}
print(d)

d = { 'a' : 1 , 'b' : 2 }
print(d)
print(d['a'])

# print(d['c'])

d['c']=3
print(d)
print(d['c'])

d['a'] = 100
print(d)

print(d.keys())
print(d.values())
print(d.items())
