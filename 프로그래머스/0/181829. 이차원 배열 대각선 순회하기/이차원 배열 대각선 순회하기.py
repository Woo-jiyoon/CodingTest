def solution(board, k):
    answer = 0
    # 행(row) 순회
    for i in range(len(board)):
        # 열(col) 순회
        for j in range(len(board[i])):
            # 조건: 행 인덱스 + 열 인덱스가 k 이하인 경우
            if i + j <= k:
                answer += board[i][j]
    return answer