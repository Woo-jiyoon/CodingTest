def solution(num_list):
    answer = 0
    for num in num_list:
        # num이 1이 될 때까지 무조건 2로 나눔
        while num > 1:
            num //= 2
            answer += 1
    return answer