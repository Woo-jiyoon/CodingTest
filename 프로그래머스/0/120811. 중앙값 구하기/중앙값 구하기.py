def solution(array):
    
    # 리스트를 오름차순으로 정렬
    array.sort()
    
    # 리스트 길이의 절반(몫)을 구하면 가운데 인덱스가 됨
    middle_index = len(array) // 2
    
    # 가운데 인덱스의 값을 반환
    return array[middle_index]