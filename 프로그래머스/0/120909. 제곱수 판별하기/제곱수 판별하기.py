def solution(n):
    
    # n의 제곱근을 구함
    sqrt_n = n ** 0.5
    
    if sqrt_n == int(sqrt_n):
        return 1
    
    else:
        return 2