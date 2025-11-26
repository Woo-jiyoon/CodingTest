def solution(n):
    answer = []
    
    # 1부터 n까지 모든 숫자를 하나씩 확인
    # range(시작, 끝 + 1) -> 1 ~ n
    for i in range(1, n + 1):
        
        # n을 i로 나누었을 때 나머지가 0이면 약수
        if n % i == 0:
            
            # 약수 리스트에 추가
            answer.append(i)
            
    return answer