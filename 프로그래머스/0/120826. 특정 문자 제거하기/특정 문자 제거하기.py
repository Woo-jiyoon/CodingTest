def solution(my_string, letter):
    
    # my_string에서 letter을 찾아 모두 빈 문자열로 바꿈 (replace)
    answer = my_string.replace(letter, '')
    return answer