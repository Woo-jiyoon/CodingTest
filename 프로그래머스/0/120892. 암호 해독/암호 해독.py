def solution(cipher, code):
    
    # 슬라이싱 구문 [start : end : step]을 활용함
    # start : code - 1 (컴퓨터 인덱스는 0부터 시작이므로 1을 뺌)
    # end 생략 (끝까지 확인해야 함)
    # step (code 간격으로 건너뜀)
    
    return cipher[code-1: :code]