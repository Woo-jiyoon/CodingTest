def solution(arr, idx):
    # 문제 설명과 달리, 입출력 예시(3번)를 보면 idx 위치부터 포함해서 찾아야 함
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1