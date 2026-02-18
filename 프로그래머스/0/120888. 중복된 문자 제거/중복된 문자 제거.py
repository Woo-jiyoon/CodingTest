def solution(my_string):
    answer = ''
    for char in my_string:
        # 이미 결과 문자열에 들어있는 문자가 아니라면 추가
        if char not in answer:
            answer += char
    return answer