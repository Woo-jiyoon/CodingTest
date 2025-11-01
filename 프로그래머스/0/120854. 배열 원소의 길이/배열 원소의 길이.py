def solution(strlist):
    answer = []
    
    # strlist에 있는 모든 문자열을 확인
    for s in strlist:
        
    # s의 길이를 확인 후 answer 리스트에 추가
        answer.append(len(s))
        
    return answer


# return [len(s) for s in strlist] 컴프리헨션으로 이렇게도 표현 가능