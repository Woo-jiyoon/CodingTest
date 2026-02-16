def solution(n):
    answer = 0
    # 1부터 n까지 각 숫자 i를 검사
    for i in range(1, n + 1):
        count = 0
        # i의 약수 개수 세기
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        
        # 약수가 3개 이상이면 합성수
        if count >= 3:
            answer += 1
    return answer