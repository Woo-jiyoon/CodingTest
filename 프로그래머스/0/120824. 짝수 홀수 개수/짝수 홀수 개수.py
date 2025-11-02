def solution(num_list):
    odd_count = 0       # 홀수 카운트
    even_count = 0      # 짝수 카운트
    
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        
        else: 
            odd_count += 1
            
    return [even_count, odd_count]