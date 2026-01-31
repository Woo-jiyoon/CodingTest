def solution(n):
    pizza = 1
    # 피자 조각(pizza * 6)이 사람 수(n)로 나누어떨어질 때까지 반복
    while (pizza * 6) % n != 0:
        pizza += 1
    return pizza