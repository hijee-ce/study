# https://school.programmers.co.kr/learn/courses/30/lessons/12941

# 공백 이후에 나오는 문자만 대문자로, 그 외 문자는 소문자로 바꿔서 출력
# 모두 소문자로 변환한 뒤, 공백 다음것만 대문자로 바꿔주기

def solution(s):
    s = s.lower()
    s = s.split(' ')
    answer = []
    
    for i in s :
        i = i[0].upper() + i[1:]
        # i = i.capitalize()
        answer.append(i)
    return ' '.join(answer)
