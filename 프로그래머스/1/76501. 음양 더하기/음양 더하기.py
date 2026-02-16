def solution(absolutes, signs):
    answer = 0
    # 두 리스트를 묶어서(val, sign) 하나씩 꺼냄
    for val, sign in zip(absolutes, signs):
        if sign: # sign이 True인 경우
            answer += val
        else:    # sign이 False인 경우
            answer -= val
    return answer