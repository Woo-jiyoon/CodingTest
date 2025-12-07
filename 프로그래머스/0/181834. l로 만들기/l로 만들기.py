def solution(myString):
    # 리스트 컴프리헨션과 삼항 연산자를 사용한 한 줄 풀이
    # 문자(x)가 "l"보다 작으면(앞선다면) "l"로 바꾸고, 아니면 그대로 둡니다.
    return "".join(["l" if x < "l" else x for x in myString])