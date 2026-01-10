import math

def solution(num_list):
    # 길이가 11 이상이면 합(sum), 아니면 곱(prod)
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return math.prod(num_list)