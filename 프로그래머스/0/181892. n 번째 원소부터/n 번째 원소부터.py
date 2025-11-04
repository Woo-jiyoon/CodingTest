def solution(num_list, n):
    
    # n번째 원소는 n-1에 위치하고 있음
    # n-1번부터 슬라이싱 진행
    answer = num_list[n-1:]
    return answer