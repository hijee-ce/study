'''
람다 함수 == 익명 함수
'''

'''
원래 함수 정의 방법
def plus_one(x):
    return x+1

print(plus_one(1))
'''


'''
lambda 매개변수: 리턴값

plus_two = lambda x: x+2 
print(plus_two(1))
'''

def plus_one(x):
    return x+1

a=[1,2,3]
print(list(map(plus_one, a)))
# map(함수, 자료) => a라는 값에 plus_one을 적용시켜라

print(list(map(lambda x : x+1, a)))
# 인자로 함수를 쓰고싶을 때 간단하게 lambda 함수 쓰는 것 
