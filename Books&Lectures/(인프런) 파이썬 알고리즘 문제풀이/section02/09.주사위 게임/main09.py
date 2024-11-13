import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/09.주사위 게임/input09.txt", 'rt')

n = int(input())

res = 0

for i in range(n):
    tmp = input().split() # 문자 형태로 만들어짐 ex ['3', '3', '6']
    tmp.sort() # 오름차순으로 정렬
    a, b, c = map(int, tmp) # tmp에 들어있는 값을 int로 형변환해서 a, b, c에 매핑
    
    if a==b and b==c :
        money = 10000 + a * 1000
    elif a==b or a==c:
        money = 1000 + a * 100
    elif b==c:
        money = 1000 + b * 100
    else:
        money = c * 100
    if money > res:
        res = money

print(res)