def solution(my_string, s, e):
    # 처음부터 s 이전까지 자르기: my_string[:s]
    # s부터 e까지 잘라서 뒤집기: my_string[s:e+1][::-1]
    # e 이후부터 끝까지 자르기: my_string[e+1:]
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]