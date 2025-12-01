def solution(n):
    # 콜라츠 수열 문제
    # 시작 값 n을 리스트에 먼저 담고 시작
    answer = [n]
    
    # n이 1이 될 때까지 무한히 반복함
    while n != 1:
        
        # 짝수라면 2로 나눔
        if n % 2 == 0:
            n = n // 2
        
        # 홀수라면 3을 곱하고 1을 더함
        else:
            n = 3 * n + 1
            
        # 계산된 n을 리스트에 추가함
        answer.append(n)
        
    return answer