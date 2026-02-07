def solution(n):
    ls = list(str(n)) # 문자열 리스트로 변환
    ls.sort(reverse=True) # 내림차순 정렬
    return int("".join(ls)) # 합쳐서 정수로 반환