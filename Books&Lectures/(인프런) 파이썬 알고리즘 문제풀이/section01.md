## 파이썬 기본 문법

<details>
<summary> 연산자 </summary>

```python
print('a+b')
print('a-b')
print('a*b')
print('a/b')    # 나누기
print('a//b')   # 몫 연산
print('a%b')    # 나머지 연산
print('a**b')   # 거듭제곱 (a의 b승)

```

</details>

<details>
<summary> 조건문 if </summary>

```python
if 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문: # 조건이 여러개인 경우 사용 (개수 제한 없음!)
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
...
else: # 위에 나온 조건들을 모두 만족하지 않을 때 실행
   수행할_문장1
   수행할_문장2
   ...
```

</details>

<details>
<summary> 반복문 for / while </summary>

```python

 for 변수 in 컬렉션: #컬렉션 : 리스트, 문자열, 튜플, range 등
    반복해서 수행할 코드

for i in range(10, 0, -1):
    print(i) # 10부터 0까지 1씩 감소하면서 출력

for i in range(1, 11):
    if i%2 == 0:
        continue # 제어 흐름은 유지, 하위 코드를 실행하지 않고 건너뜀 => 다음 루프로 넘어가서 반복문 계속 실행
    print(i)
```

```python

 while 조건:
    조건이 참인동안 반복해서 수행할 코드

i = 1
while True:
    print(i)
    if i == 10:
        break   # 제어 흐름을 중단 ==> 반복문 종료
    i += 1


```

</details>

<details>
<summary> 문자열과 내장함수 </summary>

```python
msg = "It is Time"

msg.upper()     # 모두 대문자로 변경
msg.lower()     # 모두 소문자로 변경
msg.find("T")   # 가장 처음 찾은 T의 인덱스값 반환
msg.count('T')  # T의 개수 반환
len(msg)        # msg의 길이 반환
ord('t')        # 문자 -> 아스키넘버
chr(65)         # 아스키넘버 -> 문자

for i in range(len(msg)):   # msg의 길이만큼 반복
    print(i, msg[i])        # 인덱스로 접근해서 문자 출력

for x in msg:   # x 자체가 msg의 문자
    print(x)    # 문자에 바로 접근 가능
```

</details>

<details>
<summary> 리스트와 내장함수 </summary>

```python
# 리스트 생성 방법
a=[]        # 빈 리스트
b=list()    # 빈 리스트
c=[1, 2, 3, 4, 5]       # 값, 길이 지정
d=list(range(1, 11))    # 길이 지정

c.append(6)     # 맨 뒤에 값 추가
c.insert(3, 7)  # 3번 인덱스에 7 추가
c.pop()         # 맨 뒤 값 제거
c.pop(3)        # 3번 인덱스의 값 제거
c.remove(4)     # 값(4)을 찾아서 제거

sum(c)  # 리스트에 들어있는 값들의 합 반환
min(c)  # 리스트의 값 중 최소값 반환
max(c)  # 리스트의 값 중 최대값 반환

c.sort()    # 리스트 정렬 (오름차순)
c.sort(reverse=True)    # 리스트 정렬 (내림차순)

c.clear()   # 리스트 초기화 => 빈 리스트가 됨


for x in eumerate(c):   # 인덱스와 값을 튜플 형태로 반환
    print(x)    # (0,1), (1,2) ...
    print(x[0], x[1]) # 0,1 / 1,2 / ...
```

</details>

<details>
<summary> 2차원 리스트 생성과 접근 </summary>

```python
a=[[0]*2 for _ in range(3)] # 값이 0으로 초기화된 2행 3열짜리 2차원 리스트 생성
'''
    열1 열2 열3
행 0 [] [] []
행 1 [] [] []
'''
```

</details>

<details>
<summary> 함수 만들기 </summary>

특정 기능을 반복해야할 때, 함수를 만들어서 필요한 곳에서 호출해서 사용
=> 호출하는 코드 전에 함수가 있어야 함

```python
def add(a, b):
    c=a+b
    return c

print(add(2, 3))
```

</details>

<details>
<summary> 람다 함수 </summary>

`lambda 매개변수 : 리턴값`

람다 함수 == 익명 함수
인자로 함수를 쓰고싶을 때 주로 사용

```python
a=[1, 2, 3]
print(list(map(lambda x : x+1, a)))

'''
map(함수, 데이터 집합)
데이터 집합의 각 요소에 대해 함수를 적용한 결과를 새로운 데이터 집합으로 반환
'''
```

</details>
