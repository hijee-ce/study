import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/01.K번째 약수/input.txt", 'r')

n, k = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    if n%i==0:
        cnt += 1
    if cnt == k:
        print(i)
        break
        # break를 하지 않으면 for문이 끝날때까지 반복됨 => 최소 약수 이후의 수들도 같이 출력됨
else:
    print(-1)