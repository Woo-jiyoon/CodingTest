def solution(numbers, direction):
    if direction == "right":
        # 맨 뒤의 것을 맨 앞으로 가져옴 + 처음부터 맨 뒤 직전까지
        return [numbers[-1]] + numbers[:-1]
    else:
        # 두 번째부터 끝까지 + 맨 앞의 것을 맨 뒤로 보냄
        return numbers[1:] + [numbers[0]]