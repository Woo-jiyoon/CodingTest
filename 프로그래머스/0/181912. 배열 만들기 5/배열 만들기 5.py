def solution(intStrs, k, s, l):
    answer = []
    for string in intStrs:
        # s번 인덱스부터 길이 l만큼 잘라냄
        sliced_str = string[s:s+l]
        
        # 정수로 변환
        num = int(sliced_str)
        
        # k보다 큰지 비교하고 크면 결과 리스트에 추가
        if num > k:
            answer.append(num)
            
    return answer