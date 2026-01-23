def solution(arr):
    n = len(arr)
    # 2차원 배열 전체 순회
    for i in range(n):
        for j in range(n):
            # 대칭 위치의 값이 다르면 즉시 0 반환
            if arr[i][j] != arr[j][i]:
                return 0
    # 끝까지 통과했다면 모두 대칭이므로 1 반환
    return 1