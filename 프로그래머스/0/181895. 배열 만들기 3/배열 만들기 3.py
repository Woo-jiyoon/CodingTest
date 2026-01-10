def solution(arr, intervals):
    # 첫 번째 구간 (intervals[0]) 언패킹
    a1, b1 = intervals[0]
    # 두 번째 구간 (intervals[1]) 언패킹
    a2, b2 = intervals[1]
    
    # 슬라이싱 후 이어 붙이기
    # b1, b2까지 포함해야 하므로 슬라이싱 끝에는 +1을 해줌
    return arr[a1:b1+1] + arr[a2:b2+1]