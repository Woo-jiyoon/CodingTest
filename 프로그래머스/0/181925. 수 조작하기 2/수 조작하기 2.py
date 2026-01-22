def solution(numLog):
    answer = ''
    # 변화량에 따른 조작키 매핑
    joystick = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    
    # 1번 인덱스부터 끝까지 돌면서 앞뒤 차이를 구함
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        answer += joystick[diff]
        
    return answer