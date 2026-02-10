def solution(a, d, included):
    answer = 0
    # i: 인덱스(0, 1, 2...), flag: included의 값(True/False)
    for i, flag in enumerate(included):
        if flag: # True인 경우에만
            answer += a + (d * i) # 등차수열 항을 더함
    return answer