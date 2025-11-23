def solution(my_string):
    answer = ''
    
    # 문자열을 한 글자씩 확인
    for char in my_string:
        
        # 대문자라면 소문자로 바꿔줌
        if char.isupper():
            answer += char.lower()
        
        # 소문자라면 대문자로 바꿔줌
        else:
            answer += char.upper()
            
    return answer