def solution(arr):
    n = len(arr)
    # n이 이미 2의 거듭제곱인지 확인 (n & (n-1) == 0)
    if (n & (n - 1)) == 0:
        return arr
    
    # n보다 큰 가장 가까운 2의 거듭제곱 찾기
    target = 1 << (n - 1).bit_length()
    return arr + [0] * (target - n)