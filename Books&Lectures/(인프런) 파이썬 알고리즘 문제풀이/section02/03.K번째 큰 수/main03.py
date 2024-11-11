import sys
sys.stdin=open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/03.K번째 큰 수/input03.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))

res=set() # 중복을 제거하는 자료구조 set

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res=list(res) # sort를 하기위해 Set을 다시 list에 저장해줌
res.sort(reverse=True) # 큰 수를 찾는 문제이기 때문에 내림차순으로 정렬

print(res[k-1])