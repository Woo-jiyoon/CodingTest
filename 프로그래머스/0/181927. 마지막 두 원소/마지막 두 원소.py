def solution(num_list):
    
    # 리스트의 마지막 원소
    last = num_list[-1]
    
    # 리스트의 마지막 직전 원소
    prev = num_list[-2]
    
    # 마지막 원소가 마지막 직전 원소보다 크면
    # 리스트에 last 값에서 prev 값을 뺸 값을 append
    if last > prev:
        num_list.append(last - prev)
        
    # 마지막 원소가 마지막 직전 원소보다 크지 않은 경우
    # 마지막 원소를 *2한 값을 append
    else:
        num_list.append(last * 2)
        
    return num_list