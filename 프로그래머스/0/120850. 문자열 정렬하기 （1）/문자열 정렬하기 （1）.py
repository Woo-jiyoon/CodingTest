def solution(my_string):
    
    # 숫자를 담을 빈 리스트 생성
    answer = []
    
    # 문자열의 모든 글자를 하나씩 확인
    for char in my_string:
    
        # 현재 글자가 숫자인지 확인
        if char.isdigit():
            
            # 숫자라면 정수로 변환하여 리스트에 추가
            answer.append(int(char))
            
    # 리스트를 오름차순으로 정렬
    answer.sort()
    
    # 정렬된 리스트를 반환
    return answer
   