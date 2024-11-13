import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/07.소수/input07.txt", 'rt')

n = int(input) 

ch = [0] *(n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt +=1
        for j in range(i, n+1, i): # i의 배수를 찾아 카운팅해야하니까 증가조건을 i로 주는 것
            ch[j] = 1

print(cnt)
