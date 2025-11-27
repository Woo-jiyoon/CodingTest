def solution(my_string):
    
    # .lower()로 모두 소문자로 변환
    # sorted()로 알파벳 순서 정렬(결과는 리스트가 됨)
    # "".join()으로 리스트를 다시 문자열로 합침
    
    return "".join(sorted(my_string.lower()))