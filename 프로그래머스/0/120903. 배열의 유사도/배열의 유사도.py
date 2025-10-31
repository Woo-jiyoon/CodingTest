def solution(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    
    # & 연산자로 두 set의 교집합을 구함
    common = set1 & set2
    
    # len() 함수로 교집합의 원소 개수 출력
    return len(common)