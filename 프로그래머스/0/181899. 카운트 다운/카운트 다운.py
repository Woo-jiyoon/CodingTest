def solution(start_num, end_num):
    answer = []
    # start부터 end까지 거꾸로 반복
    for i in range(start_num, end_num - 1, -1):
        answer.append(i)
    return answer