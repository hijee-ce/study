import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section03 탐색 & 시뮬레이션/02. 숫자만 추출/input02.txt", 'rt')

s=input()
res=0
for x in s:
    if x.isdecimal(): # 0-9까지만 찾음
    # isdigit() # 숫자를 모두 찾아줌
        res = res*10 + int(x)
print(res)

cnt = 0
# 약수의 개수 구하는 과정
for i in range(1, res+1):
    if res%i==0:
        cnt += 1
print(cnt)