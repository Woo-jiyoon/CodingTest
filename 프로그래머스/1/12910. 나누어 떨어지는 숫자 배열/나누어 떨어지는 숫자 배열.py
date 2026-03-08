def solution(arr, divisor):
    # arr의 원소 중 divisor로 나누어 떨어지는 것만 추출하여 정렬
    # 만약 빈 리스트라면 거짓으로 평가되므로 뒤의 [-1]이 반환
    return sorted([n for n in arr if n % divisor == 0]) or [-1]