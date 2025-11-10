def solution(a, b):
    
    # a와 b를 문자열로 변환 후 더하고 다시 정수형으로 변환
    ab_concat = int(str(a) + str(b))
    
    # b와 a를 문자열로 변환 후 더하고 다시 정수형으로 변환
    ba_concat = int(str(b) + str(a))
    
    # max 함수는 두 값이 같을 때 앞에 있는 인자를 출력함으로 문제에 알맞음
    return max(ab_concat, ba_concat)