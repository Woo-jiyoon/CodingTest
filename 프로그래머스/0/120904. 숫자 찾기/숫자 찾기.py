def solution(num, k):
    # 정수 num과 k를 문자열로 변환함
    s_num = str(num)
    s_k = str(k)
    
    # find() 함수로 k가 위치한 인덱스를 찾음
    # (찾으면 0부터 시작하는 인덱스 반환 없으면 -1 반환)
    index = s_num.find(s_k)
    
    # k를 찾지 못했다면(index가 -1이면) 그대로 -1 반환
    if index == -1:
        return -1
    # 찾았다면 문제 요구사항(1부터 시작)에 맞춰 +1 해서 반환
    else:
        return index + 1