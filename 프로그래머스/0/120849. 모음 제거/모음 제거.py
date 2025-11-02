def solution(my_string):
    vowels = 'aeiou'
    answer = my_string
    
    # empty에 있는 모음을 하나씩 확인
    for v in vowels:
    
    # answer 문자열에서 해당 모음을 찾아 ''로 변환
        answer = answer.replace(v, '')
    return answer