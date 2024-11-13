import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/10.점수계산/input10.txt", 'rt')

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for i in a:
    if i == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)