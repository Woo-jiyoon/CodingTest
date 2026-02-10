def solution(n):
    # reversed(str(n))으로 뒤집힌 반복자(iterator)를 만들고
    # map(int, ...)로 각각 정수로 변환 후 list로 묶음
    return list(map(int, reversed(str(n))))