def solution(numbers):
    answer = 0
    # 0부터 9까지 하나씩 확인
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer