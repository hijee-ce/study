import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/01.K번째 약수/input.txt", 'r')

n, k = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    if n%i==0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)