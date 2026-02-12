def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10 # 1의 자리 숫자를 더함
        n //= 10 # 10으로 나누어 자릿수를 줄임 (몫만 취함)
    return answer