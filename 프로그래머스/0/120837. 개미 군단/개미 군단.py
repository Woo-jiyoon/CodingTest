def solution(hp):
    
    # 장군 개미로 최대한 처리 (공격력 5)
    general = hp // 5
    
    # 장군 개미가 처리하고 남은 체력
    hp = hp % 5
    
    # 병정 개미로 최대한 처리 (공격력 3)
    soldier = hp // 3
    
    # 병정 개미까지 처리하고 남은 체력
    hp = hp % 3
    
    # 남은 체력은 일개미가 처리 (공격력 1)
    # 공격력이 1이므로 남은 체력 수 = 일개미 수와 같음
    worker = hp
    
    # 총 필요한 개미 수 반환
    return general + soldier + worker