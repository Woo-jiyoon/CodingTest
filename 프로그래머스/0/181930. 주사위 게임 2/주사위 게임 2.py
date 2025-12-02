def solution(a, b, c):

    # 세 숫자를 집합(set)으로 만듦
    # 예: {1, 1, 2} -> {1, 2} (길이 2)
    unique_nums = set([a, b, c])
    count = len(unique_nums)
    
    # 집합의 길이(고유한 숫자의 개수)에 따라 점수를 계산함
    # Case 1: 세 숫자가 모두 다름 (집합 길이 3)
    if count == 3:
        return a + b + c
        
    # Case 2: 두 숫자는 같고 하나만 다름 (집합 길이 2)
    elif count == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
        
    # Case 3: 세 숫자가 모두 같음 (집합 길이 1)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)