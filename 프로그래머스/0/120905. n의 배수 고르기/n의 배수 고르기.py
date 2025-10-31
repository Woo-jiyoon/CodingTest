def solution(n, numlist):
    answer = []
    
    # numlist에 있는 모든 숫자를 하나씩 확인
    for num in numlist:
    
    # 만약 숫자가 n으로 나누어 떨어지면 n의 배수
        if num % n == 0:
    # answer 리스트에 추가
            answer.append(num)
            
    return answer