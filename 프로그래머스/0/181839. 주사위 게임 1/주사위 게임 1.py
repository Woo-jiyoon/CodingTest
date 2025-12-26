def solution(a, b):
    # 두 주사위가 모두 홀수인 경우
    if a % 2 != 0 and b % 2 != 0:
        return a**2 + b**2
    
    # 두 주사위 중 하나만 홀수인 경우
    # (위의 if문을 통과하지 못했으므로, 둘 다 홀수인 경우는 이미 제외됨)
    elif a % 2 != 0 or b % 2 != 0:
        return 2 * (a + b)
        
    # 두 주사위가 모두 홀수가 아닌 경우 (모두 짝수인 경우)
    else:
        return abs(a - b)