def solution(n_str):
    # 문자를 숫자로 바꾸면 앞의 0이 자동으로 사라짐 (0010 -> 10)
    # 그것을 다시 문자로 바꿈 (10 -> "10")
    return str(int(n_str))