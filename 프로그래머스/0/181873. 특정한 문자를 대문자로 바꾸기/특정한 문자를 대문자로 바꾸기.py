def solution(my_string, alp):
    # my_string 안에 있는 모든 alp(소문자)를
    # alp.upper()(대문자)로 찾아서 바꿈(replace)
    return my_string.replace(alp, alp.upper())