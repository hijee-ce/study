import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section03 탐색 & 시뮬레이션/01. 회문 문자열 검사/input01.txt", 'rt')

n = int(input())

for i in range(n):
    str = input().lower()
    '''
    # reverse 과정을 직접 구현
    size = len(str)
    
    for j in range(size//2):
        if str[j] != str[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
    '''
    
    # 인덱스 슬라이싱을 활용해 간단하게 구현
    if str==str[::-1] :# [::-1] 맨 뒷자리부터 -1씩 접근하면서 문자열을 뒤집어줌
        print("#%d YES" %(i+1))
    else : print("#%d NO" %(i+1))