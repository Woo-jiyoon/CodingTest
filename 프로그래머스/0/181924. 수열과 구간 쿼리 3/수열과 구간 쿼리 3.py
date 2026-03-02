def solution(arr, queries):
    # queries에서 [i, j] 쌍을 하나씩 꺼냄
    for i, j in queries:
        # 스왑 문법을 사용해 arr[i]와 arr[j]의 값을 맞바꿈
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr