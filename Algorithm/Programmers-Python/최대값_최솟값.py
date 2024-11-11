# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    number = list(map(int, s.split()))
    return str(min(number)) + " " +str(max(number))