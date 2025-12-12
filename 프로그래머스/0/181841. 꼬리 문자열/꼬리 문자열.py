def solution(str_list, ex):
    answer = ''
    
    # 리스트의 문자열을 하나씩 꺼내서 확인
    for s in str_list:
        # ex가 s에 포함되어 있지 않다면(not in)
        if ex not in s:
            # 결과 문자열에 이어 붙임
            answer += s
            
    return answer