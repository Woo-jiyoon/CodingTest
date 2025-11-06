def solution(n):
    answer = 0
    
    # 홀수인 경우 1부터 n까지 2씩 건너뜀
    # 그냥 합을 구함
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            answer += i
            
    # 짝수인 경우 2부터 n까지 2씩 건너뜀    
    # 제곱의 합을 구함
    else:
        for i in range(2, n+1, 2):
            answer += i ** 2
            
    return answer
        