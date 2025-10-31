def solution(money):
    price = 5500
    
    # 마실 수 있는 잔
    coffee = money // price
    
    # 커피 구매 후 남은 돈
    change = money % price
    
    return [coffee, change]