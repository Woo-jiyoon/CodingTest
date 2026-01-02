def solution(strArr):
    # i: 인덱스, s: 문자열
    # 짝수 인덱스(i%2==0)면 소문자, 아니면(홀수) 대문자
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]