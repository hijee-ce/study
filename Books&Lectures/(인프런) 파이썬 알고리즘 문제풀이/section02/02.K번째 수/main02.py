import sys
sys.stdin = open("Books&Lectures/(인프런) 파이썬 알고리즘 문제풀이/section02/02.K번째 수/input02.txt", 'rt')

T=int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a = a[s-1 : e]
    a.sort()
    
    print("#%d %d" %(t+1, a[k-1]))
    

'''
sys.stdin.input() : 개행 문자 (\n)을 삭제시켜 반환  | 값을 입력할 때마다 버퍼에 저장
sys.stdin.readline() : 개행 문자 (\n)을 포함시켜 반환 | 한번에 읽어서 버퍼에 저장 => 입력이 많은 경우 우위를 가짐

# input()의 입력 저장 순서
1. input이 호출되면 인자로 주어진 prompt 문자열을 화면에 출력하고 사용자의 입력을 기다림 (표준입력은 키보드)
2. 사용자가 키를 하나씩 누르면 이에 대응하는 데이터가 버퍼에 들어감
3. enter키를 누르면 개행문자가 입력되며, 버퍼의 입력이 종료된 것으로 간주
4. 입력된 문자열은 해당 시스템의 콘솔 입출력 인코딩을 사용하여 디코드되어 유니코드 문자열로 반환
6. input()함수는 변환된 문자열 값을 반환하면서 종료됨

=> 개행문자 (enter, \n)을 기준으로 값을 가져오는 함수
'''


'''
리스트 인덱싱
 a[s:e] => 인덱스 s부터 e전까지 슬라이싱!! (e는 포함되지 않는 것이 포인트)
 
 위 문제 : s번째부터 e번째 숫자를 정렬
    인덱스로 변환하면 s-1번부터 e-1번까지가 필요
    => 슬라이싱하면 [s-1:e]까지가 되는 것!
'''

'''
sort() sorted()의 차이
sort() : 리턴값이 없음   | list의 값들을 변경시킴
sorted() : 리턴값이 있음 | 새로운 list를 리턴

 ex) a = a[s-1 : e].sort()
    => a를 출력해보면 None : sort()는 리턴값이 없으므로
'''