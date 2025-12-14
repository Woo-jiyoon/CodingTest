def solution(str1, str2):
    # str1이 str2 안에 포함되어 있다면 (True)
    if str1 in str2:
        return 1
    # 포함되어 있지 않다면 (False)
    else:
        return 0