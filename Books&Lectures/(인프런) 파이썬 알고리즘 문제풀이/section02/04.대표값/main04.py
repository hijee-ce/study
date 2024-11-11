import sys
sys.stdin=open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/04.대표값/input04.txt", 'rt')

n=int(input())
a=list(map(int, input().split()))

ave = round(sum(a)/n) 
min=2147000000 # 임의로 가장 큰 값을 넣어줌 (4byte 정수형에서 가장 큰 숫자)

for idx, x in enumerate(a):
    tmp=abs(x-ave) # 차이를 절대값으로 구함
    
    if tmp<min:
        min=tmp
        score=x
        res=idx+1 #인덱스값이니까 +1
    elif tmp==min:
        if x > score : # x : 현재 학생의 점수 / score : 이전 학생의 점수
            score=x
            res=idx+1

print(ave, res)
    
    
'''
eumerate()
: 인덱스, 값을 쌍으로 대응해주는 함수
'''

'''
파이썬의 round함수는 round_half_even 방식

a=4.500
print(round(a)) => 4가 출력됨
b=5.5000
print(round(b)) => 6이 출력됨

정확하게 half 지점에 있다? => 짝수 쪽으로 값을 변경
'''