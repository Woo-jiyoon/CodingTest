def solution(n):
    
    # str(n)으로 정수 n을 문자열로 변환
    # map(int, str)을 활용해 문자열을 int 형태로 변환
    # sum 함수를 통해 만들어진 모든 숫자를 더함
    return sum(map(int, str(n)))