def solution(my_string, m, c):
    # 슬라이싱 구문: [시작:끝:간격]
    # c번째 열은 인덱스로 c-1
    # m 글자마다 같은 열이 반복되므로 간격을 m으로 설정
    return my_string[c-1::m]