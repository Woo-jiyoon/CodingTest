def solution(price):
    
    # 가장 큰 금액인 50만원부터 확인 후 20% 할인
    if price >= 500000:
        price = price * 0.8
        
    # 그 다음 큰 금액인 30만원 10% 할인
    elif price >= 300000:
        price = price * 0.9
    
    # 마지막으로 10만원 5% 할인
    elif price >= 100000:
        price = price * 0.95
    
    # 계산된 금액을 정수로 바꿔서 반환
    return int(price)