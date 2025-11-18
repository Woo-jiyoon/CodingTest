def solution(my_string):
    answer = 0
    
    
    # 문자열 my_string을 한 글자씩(char) 순회함
    for char in my_string:
        
        # .isdigit() 함수로 해당 문자가 숫자인지 판별함
        # ex) a.isdigit() -> False, 3.isdigit() -> True
        if char.isdigit():
            
            # 숫자가 맞다면 int()로 정수형으로 변환
            # answer 변수에 더해줌
            answer += int(char)
    
    # 모든 반복이 끝난 뒤 누적된 합계를 반환함
    return answer