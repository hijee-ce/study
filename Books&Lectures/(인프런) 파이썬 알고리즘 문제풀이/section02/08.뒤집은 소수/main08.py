import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/08.뒤집은 소수/input08.txt", 'rt')

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res * 10 + t
        x = x//10
    return res

def isPrime(tmp):
    if tmp == 1:
        return False
    for i in range(2, tmp//2+1):
        if tmp%i == 0: # 약수가 존재한다는 의미
            return False
    else: return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp)
        
        
'''
isPrime() 에서 tmp//2 까지만 반복하는 이유
    약수는 항상 대칭성을 가짐
    ex) 36의 약수 : 1 2 3 4 6 9 12 18 36
    => 6을 기준으로 짝을 이루고 있음 (1,36) (2, 18) (3, 12) (4, 9) (6, 6)
    
    따라서 tmp//2까지 반복했는데도 약수가 없다면? 그 이상에도 약수가 없다!
'''