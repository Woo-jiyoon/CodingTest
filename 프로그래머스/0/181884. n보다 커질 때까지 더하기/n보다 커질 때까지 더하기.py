def solution(numbers, n):
    answer = 0
    for num in numbers:
        answer += num  # 하나씩 더함
        if answer > n: # n보다 커지는 순간
            return answer # 바로 반환하고 종료
    return answer