def solution(a, b):
    # 작은 수부터 큰 수까지 range를 생성하여 합계 구하기
    return sum(range(min(a, b), max(a, b) + 1))