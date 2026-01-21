def solution(my_string):
    answer = []
    # 0부터 끝까지 반복하며 접미사 생성
    for i in range(len(my_string)):
        answer.append(my_string[i:]) # i번째부터 끝까지 자르기
    
    # 사전순으로 정렬
    answer.sort()
    return answer