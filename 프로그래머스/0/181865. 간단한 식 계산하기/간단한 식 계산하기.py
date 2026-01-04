def solution(binomial):
    # 공백을 기준으로 문자열을 나눔
    # (예: "43 + 12" -> "43", "+", "12")
    a, op, b = binomial.split()
    
    # 숫자 부분은 정수(int)로 변환
    a = int(a)
    b = int(b)
    
    # 연산자(op)에 따라 계산
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b