def solution(n):
    # 1. n x n 크기의 0으로 채워진 2차원 리스트 생성
    answer = [[0] * n for _ in range(n)]
    
    # 2. 대각선 위치(i, i)만 1로 변경
    for i in range(n):
        answer[i][i] = 1
        
    return answer