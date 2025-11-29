def solution(my_string, is_prefix):
    
    # startswith()는 True / False를 반환함
    # int()를 감싸서 1(True) 또는 0(False)로 변환
    return int(my_string.startswith(is_prefix))

    # 접두사는 startswith()
    # 접미사는 endswith()