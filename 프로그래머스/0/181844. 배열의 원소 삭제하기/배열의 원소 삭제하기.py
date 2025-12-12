def solution(arr, delete_list):
    # arr의 원소(x) 중에서 delete_list에 없는(not in) 것만 남김
    return [x for x in arr if x not in delete_list]