def solution(num_list, n):
    # n이 num_list 안에 있다면 1을, 아니면 0을 반환함
    if n in num_list:
        return 1
    else:
        return 0