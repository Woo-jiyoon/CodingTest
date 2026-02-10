def solution(n):
    # 제곱근 구하기 (n의 0.5승)
    sqrt = n ** 0.5
    
    # 정수 판별: 1로 나눈 나머지가 0이면 정수
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    
    # 정수가 아니면 -1 반환
    return -1