def solution(n, k):
    # k부터 n까지 k 간격으로 숫자를 생성하여 리스트로 만듦
    return list(range(k, n + 1, k))