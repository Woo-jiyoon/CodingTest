def solution(before, after):
    # before와 after를 각각 정렬한 리스트가 서로 같다면 1 다르면 0을 반환
    return 1 if sorted(before) == sorted(after) else 0