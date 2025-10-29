def solution(array, height):
    
    # array에서 1개씩 꺼낸 후 h에 저장
    # h가 height보다 크면 1씩 더함
    answer = sum(1 for h in array if h > height)
    return answer