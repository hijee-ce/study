import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/06.자릿수의 합/input06.txt", 'rt')

n = int(input())

a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    '''
    # 방법 1)
     while x > 0 : # x(10으로 나눈 몫)가 0이 되면 while문 종료
        sum += x%10 # 10으로 나눈 나머지를 누적
        x= x//10 # 10으로 나눈 몫을 x에 대입
    return sum   
    '''
    
    # 방법 2) x를 string으로 바꿔서 문자 하나하나에 접근
    for i in str(x):
        sum=int(i)
    return sum
    
max= -2147000000

for x in a:
    total = digit_sum(x) # sum을 반환받음
    if total > max:
        max=total
        res=x
print(res)