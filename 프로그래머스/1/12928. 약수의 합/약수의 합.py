def solution(n):
    answer = 0
    # 1부터 n까지 순회
    for i in range(1, n + 1):
        if n % i == 0: # 약수 판별
            answer += i
    return answer