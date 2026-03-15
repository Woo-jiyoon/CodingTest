def solution(num):
    answer = 0
    
    # num이 1이 될 때까지 반복
    while num != 1:
        # 500번 반복해도 1이 되지 않으면 -1을 반환하고 종료
        if answer >= 500:
            return -1
        
        # 입력된 수가 짝수라면 2로 나눔
        if num % 2 == 0:
            num //= 2
        # 입력된 수가 홀수라면 3을 곱하고 1을 더함
        else:
            num = (num * 3) + 1
            
        # 작업 횟수를 1 증가
        answer += 1
        
    return answer