def solution(num_list, n):
    # 0부터 num_list의 끝까지 n칸씩 건너뛰며 인덱스 i를 만듦
    # i부터 i+n까지 잘라낸 리스트를 새로운 2차원 리스트 안에 담음
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]