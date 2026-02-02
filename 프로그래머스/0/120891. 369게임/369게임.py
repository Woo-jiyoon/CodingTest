def solution(order):
    # 숫자를 문자열로 변환
    s_order = str(order)
    # 3의 개수 + 6의 개수 + 9의 개수
    return s_order.count('3') + s_order.count('6') + s_order.count('9')