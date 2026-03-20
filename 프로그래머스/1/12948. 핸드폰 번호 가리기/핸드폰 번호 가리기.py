def solution(phone_number):
    # '*' * (전체 길이 - 4) : 뒷 4자리를 뺀 나머지 길이만큼 '*'을 만듦
    # phone_number[-4:] : 문자열의 맨 뒤에서 4번째부터 끝까지 잘라냄
    # 이 둘을 더해줌
    return '*' * (len(phone_number) - 4) + phone_number[-4:]