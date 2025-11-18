def solution(rsp):
    
    # 딕셔너리에 승리 규칙을 정의함 (Key : 상대, Value : 승리)
    # 매핑(Mapping) 치환을 이용하여 문자열 치환
    rules = {
        '2':'0',  # 가위(2)를 이기는 것은 바위(0)
        '0':'5',  # 바위(0)을 이기는 것은 보(5)
        '5':'2'   # 보(5)를 이기는 것은 가위(2)
    }
    
    result = "" # 결과를 누적할 빈 문자열을 초기화함
    
    # 입력 문자열 rsp를 한 글자씩 순회함
    for char in rsp:
        
        # 딕셔너리에서 char에 해당하는 승리 값(Value)를 찾음
        win_hand = rules[char]
        
        # 찾은 승리 값을 result 문자열에 이어 붙임
        result += win_hand
    
    return result