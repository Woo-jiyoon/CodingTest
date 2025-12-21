def solution(num_str):
    answer = 0
    # 문자열에서 글자를 하나씩 꺼냄
    for s in num_str:
        # 정수로 변환해서 더함
        answer += int(s)
    return answer