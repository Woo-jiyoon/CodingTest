def solution(my_string, num1, num2):
    
    # 문자열은 수정이 불가능
    # 수정이 가능한 리스트 형태로 변환
    s_list = list(my_string)
    
    
    # 파이썬의 다중 할당 문법을 사용하여 두 값을 맞바꿈
    # temp 변수 없이 한 줄로 가능 (swap 필요 x)
    s_list[num1], s_list[num2] = s_list[num2], s_list[num1]
    
    # 리스트를 다시 문자열로 합쳐 반환
    return "".join(s_list)