def solution(age):
    # 0부터 9까지 대응되는 문자를 순서대로 나열
    match = "abcdefghij"
    
    # 나이(age)를 문자열로 바꿈 (23 -> "23")
    # 각 자릿수(digit)를 정수로 바꿔 인덱스로 사용
    # 매칭된 문자를 다시 합침
    return "".join([match[int(digit)] for digit in str(age)])