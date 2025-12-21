def solution(num_list):
    # 리스트를 오름차순(작은 순서대로) 정렬함
    # 앞에서부터 5개를 제외하고(인덱스 5부터) 끝까지 자름
    return sorted(num_list)[5:]