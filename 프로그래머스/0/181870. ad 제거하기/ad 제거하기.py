def solution(strArr):
    # "ad"가 포함되지 않은(not in) 문자열만 모아서 새 리스트 생성
    return [s for s in strArr if "ad" not in s]