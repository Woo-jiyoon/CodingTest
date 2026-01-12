def solution(arr):
    answer = []
    for num in arr:
        if num >= 50 and num % 2 == 0:
            # 50 이상이면서 짝수라면 2로 나눔 (정수 나눗셈 // 사용)
            answer.append(num // 2)
        elif num < 50 and num % 2 != 0:
            # 50 미만이면서 홀수라면 2를 곱함
            answer.append(num * 2)
        else:
            # 나머지 경우는 그대로 둠
            answer.append(num)
    return answer