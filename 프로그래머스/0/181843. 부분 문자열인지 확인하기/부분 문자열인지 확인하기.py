def solution(my_string, target):
    # target이 my_string 안에 포함되어 있다면 1 반환
    if target in my_string:
        return 1
    # 아니라면 0 반환
    else:
        return 0