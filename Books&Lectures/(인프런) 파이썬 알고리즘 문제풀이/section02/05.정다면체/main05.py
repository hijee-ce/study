import sys
sys.stdin=open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/05.정다면체/input05.txt", 'rt')

n, m = map(int, input().split())
cnt = [0]*(n+m+3) # 눈의 합의 최대는 n+m / 약간의 여유를 위해 임의로 3을 더해줌
max=0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] +=1 # cnt의 인덱스 == 두 눈의 합

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')