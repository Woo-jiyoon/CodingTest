def solution(numbers):
    
    numbers.sort()
    
    # sort로 정렬을 해놨기 때문에 가장 작은 수 먼저 계산
    # 이유는 둘 다 음수일 경우 곱했을 때 양수가 되기 때문
    start = numbers[0] * numbers[1]
    
    # sort로 정렬 후 가장 큰 수 두 개의 곱
    end = numbers[-1] * numbers[-2]

    answer = max(start, end)
    return answer