def solution(myString, pat):
    # rfind(pat)을 통해 pat이 마지막으로 등장하는 시작 인덱스를 찾음
    # 문자열을 끝까지 포함해야 하므로 pat의 길이만큼 더해준 곳까지 슬라이싱함
    end_idx = myString.rfind(pat) + len(pat)
    return myString[:end_idx]