def solution(myString, pat):
    # 두 문자열을 모두 소문자로 바꾼 뒤 비교
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0