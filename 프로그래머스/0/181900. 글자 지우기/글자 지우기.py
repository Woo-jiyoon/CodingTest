def solution(my_string, indices):
    s_list = list(my_string)
    # 인덱스를 내림차순으로 정렬 (큰 것부터 지워야 인덱스가 안 꼬임)
    for i in sorted(indices, reverse=True):
        del s_list[i]
    return "".join(s_list)