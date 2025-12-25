def solution(arr1, arr2):
    # 길이 비교 (1순위)
    if len(arr1) > len(arr2):
        return 1
    elif len(arr2) > len(arr1):
        return -1
        
    # 합 비교 (2순위) - 길이가 같을 때만 여기로 옴
    else:
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        
        if sum1 > sum2:
            return 1
        elif sum2 > sum1:
            return -1
        else:
            return 0