def solution(a, b):
    
    # str()로 문자열로 만들고 붙인 뒤 int형으로 변환
    ab_concat = int(str(a) + str(b)) 
    
    # 2 * a * b 계산
    ab_product = 2 * a * b
    
    if ab_concat >= ab_product:
        return ab_concat
    
    else:
        return ab_product