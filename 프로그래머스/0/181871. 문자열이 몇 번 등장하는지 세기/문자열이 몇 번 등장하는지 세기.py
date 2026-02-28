def solution(myString, pat):
    count = 0
    pat_len = len(pat)
    
    # 0부터 전체 길이 - pat 길이까지만 순회하면 됨
    for i in range(len(myString) - pat_len + 1):
        # i부터 pat의 길이만큼 슬라이싱해서 비교
        if myString[i : i + pat_len] == pat:
            count += 1
            
    return count