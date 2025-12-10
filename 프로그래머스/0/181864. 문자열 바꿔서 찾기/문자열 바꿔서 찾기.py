def solution(myString, pat):
    # 변환된 문자열을 담을 빈 상자(변수)를 준비함
    result = ""
    
    # myString의 글자를 하나씩 꺼내서 확인함
    for char in myString:
        # 글자가 "A"라면 "B"를 결과에 추가
        if char == "A":
            result += "B"
        # 글자가 "B"라면 "A"를 결과에 추가
        else:
            result += "A"
            
    # 완성된 result 문자열 안에 pat이 있는지 확인함
    if pat in result:
        return 1
    else:
        return 0