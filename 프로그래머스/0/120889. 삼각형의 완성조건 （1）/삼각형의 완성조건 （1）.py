def solution(sides):
    
    # 가장 긴 변을 알아야 하니 sort 정렬이 필요해 보임
    sides.sort()
    
    # 세 변의 길이가 담긴 배열 sides에서 sort 후
    # 0, 1, 2 중 2에 가장 큰 수가 담김
    # 문제에 있는 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 함
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    
    else:
        answer = 2
        
    return answer