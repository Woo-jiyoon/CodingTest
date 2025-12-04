# 입력받은 문자열을 공백 기준으로 쪼개고(split) 
# map을 사용해 한 번에 정수(int)로 변환함
a, b = map(int, input().split())

# f-string을 사용하여 계산식을 보기 좋게 출력함
print(f"{a} + {b} = {a + b}")