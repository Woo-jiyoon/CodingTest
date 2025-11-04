def solution(num_list):
    
    odd_string = ''  # 홀수
    even_string = '' # 짝수
    
    for num in num_list:
        if num % 2 == 0:
            even_string += str(num)
        else:
            odd_string += str(num)
            
    return int(odd_string) + int(even_string)