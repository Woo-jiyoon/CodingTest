def solution(arr):
    # [값 for 값 in 리스트 for _ in range(값)] -> 이중 반복문을 한 줄로 표현
    return [num for num in arr for _ in range(num)]