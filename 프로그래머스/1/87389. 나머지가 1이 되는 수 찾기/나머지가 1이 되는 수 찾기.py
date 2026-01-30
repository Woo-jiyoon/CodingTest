def solution(n):
    # 1은 나눴을 때 나머지가 0이므로 2부터 n까지 반복
    for x in range(2, n):
        if n % x == 1:
            return x