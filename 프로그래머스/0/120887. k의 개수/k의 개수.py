def solution(i, j, k):
    # i부터 j까지의 숫자를 문자열로 변환하여 하나의 긴 문자열로 이어 붙임
    # 그 안에서 문자열 k가 몇 번 등장하는지 셈
    return "".join(map(str, range(i, j + 1))).count(str(k))