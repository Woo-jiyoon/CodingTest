def solution(num_list):
    
    # 모든 원소의 합을 구함
    total_sum = sum(num_list)
    
    # 합의 제곱을 구함
    square_sum = total_sum ** 2
    
    # 모든 원소의 곱
    total_product = 1
    for num in num_list:
        total_product *= num
    
    # 곱이 합의 제곱보다 작으면 1 그렇지 않으면 0을 반환
    if total_product < square_sum:
        return 1
    else: 
        return 0