def solution(arr, flag):
    X = []
    # zip을 사용해 arr와 flag의 요소를 동시에 순회
    for a, f in zip(arr, flag):
        if f: # flag가 True일 때
            # a를 a * 2 번 반복한 리스트를 X에 이어 붙임
            X += [a] * (a * 2)
        else: # flag가 False일 때
            # 뒤에서부터 a개의 원소를 잘라냄
            X = X[:-a]
    return X