def solution(str1, str2):
    answer = ''
    # 문자열의 길이가 같으므로 range를 하나만 써도 됨
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer