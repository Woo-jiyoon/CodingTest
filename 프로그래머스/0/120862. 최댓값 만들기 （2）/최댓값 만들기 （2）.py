def solution(numbers):
    
    # 리스트를 오름차순으로 정렬
    numbers.sort()
    
    # 두 가지 경우의 수를 계산
    # case1 : 가장 작은 두 수의 곱 (음수 * 음수 = 양수가 될 수 있음)
    case1 = numbers[0] * numbers[1]
    
    # case2 : 가장 큰 두 수의 곱
    case2 = numbers[-1] * numbers[-2]
    
    # 두 경우 중 더 큰 값을 반환함
    return max(case1, case2)
    