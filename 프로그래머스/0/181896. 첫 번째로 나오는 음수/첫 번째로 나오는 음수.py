def solution(num_list):
    
    # enumerate는 (인덱스, 값)을 차례대로 출력해줌
    for index, num in enumerate(num_list):
        
    # 만약 값이 0보다 작으면 index를 출력
        if num < 0:
            return index
        
    return -1