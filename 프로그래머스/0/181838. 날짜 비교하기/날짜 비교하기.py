def solution(date1, date2):
    # 파이썬의 리스트 비교는 앞에서부터 순서대로 크기를 비교함
    # date1이 date2보다 앞서는 날짜라면 1, 아니면 0
    return 1 if date1 < date2 else 0