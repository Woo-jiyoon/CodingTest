def solution(array):
    
    # 가장 큰 수를 찾아 변수에 저장
    max_num = max(array)
    
    # 그 숫자가 있는 인덱스를 찾음
    max_index = array.index(max_num)
    
    # [가장 큰 수, 인덱스] 형태로 반환
    return [max_num, max_index]