def solution(myString):
    # "x"를 기준으로 문자열을 쪼갬 (split)
    # 쪼개진 각 조각(s)의 길이를 잼 (len)
    return [len(s) for s in myString.split('x')]