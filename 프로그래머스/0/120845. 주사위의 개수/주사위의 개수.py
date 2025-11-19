def solution(box, n):
    
    # 가로, 세로, 높이에 들어가는 주사위 개수를 몫으로 계산함
    width_count = box[0] // n
    length_count = box[1] // n
    height_count = box[2] // n
    
    # 세 개의 개수를 곱해 최대 주사위 개수를 반환함
    return width_count * length_count * height_count