def solution(num_list):
    # num_list[::2] -> 인덱스 0, 2, 4... (홀수 번째 원소들)
    # num_list[1::2] -> 인덱스 1, 3, 5... (짝수 번째 원소들)
    # 각각의 합(sum)을 구한 뒤, 더 큰 값(max)을 반환
    return max(sum(num_list[::2]), sum(num_list[1::2]))