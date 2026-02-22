def solution(arr, queries):
    # queries에서 하나씩 쿼리 [s, e]를 꺼냄
    for s, e in queries:
        # 인덱스 s부터 e까지 순회하며 1씩 더해줌
        # range의 끝은 e + 1이 되어야 e까지 포함됨
        for i in range(s, e + 1):
            arr[i] += 1
            
    return arr