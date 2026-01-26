def solution(myString):
    # filter로 빈 문자열 제거 후 정렬
    return sorted(filter(None, myString.split('x')))