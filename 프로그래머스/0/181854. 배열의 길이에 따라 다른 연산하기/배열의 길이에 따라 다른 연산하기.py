def solution(arr, n):
    # arr의 길이(개수)를 잼
    length = len(arr)
    
    # 케이스 1: 길이가 홀수인 경우
    if length % 2 != 0:
        # 짝수 인덱스(0, 2, 4...)만 순회하며 n을 더함
        for i in range(0, length, 2):
            arr[i] += n
            
    # 케이스 2: 길이가 짝수인 경우
    else:
        # 홀수 인덱스(1, 3, 5...)만 순회하며 n을 더함
        for i in range(1, length, 2):
            arr[i] += n
            
    return arr