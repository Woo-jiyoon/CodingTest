def solution(my_strings, parts):
    answer = []
    # 두 리스트를 묶어서(s: 문자열, p: 구간 [s, e]) 하나씩 꺼냄
    for s, (start, end) in zip(my_strings, parts):
        # 파이썬 슬라이싱은 끝 인덱스를 포함하지 않으므로 +1을 해줌
        answer.append(s[start : end + 1])
    
    # 리스트에 담긴 조각들을 하나의 문자열로 합침
    return ''.join(answer)