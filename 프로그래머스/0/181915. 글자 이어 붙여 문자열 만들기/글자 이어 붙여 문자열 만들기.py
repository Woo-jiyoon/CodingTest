def solution(my_string, index_list):
    
    # index_list의 인덱스(idx)를 순회하며 my_string의 해당 글자를 뽑아 리스트로 만듦
    # "".join()을 사용하여 하나의 문자열로 합침
    return "".join(my_string[idx] for idx in index_list)