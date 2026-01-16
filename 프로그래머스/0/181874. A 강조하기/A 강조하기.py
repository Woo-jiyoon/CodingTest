def solution(myString):
    # 모든 문자를 소문자로 바꿈 ("PrOgRaMmErS" -> "programmers")
    # 2. 소문자 'a'를 대문자 'A'로 바꿈 ("programmers" -> "progrAmmers")
    return myString.lower().replace('a', 'A')