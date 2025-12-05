def solution(arr, k):
    # k가 홀수라면 (나머지가 0이 아님) -> 모든 원소에 k를 곱함
    if k % 2 != 0:
        return [x * k for x in arr]
    
    # k가 짝수라면 (else) -> 모든 원소에 k를 더함
    else:
        return [x + k for x in arr]