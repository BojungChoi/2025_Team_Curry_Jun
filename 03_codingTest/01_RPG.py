"""
01_ 문제

RPG 게임의 용사가 있습니다.
attack 리스트에는 피격 된 정보가 저장되어 있습니다.
-1 : 회피
0 : 골렘
1 : 리본돼지
2 : 슬라임

monsters 딕셔너리에는 몬스터별 공격력이 저장되어 있습니다.

attack 을 입력 받았을 때, 모든 공격이 끝난 후 용사의 hp를 리턴해주세요.

예외 : hp가 0이 되면 남은 공격이 있든 없든, 사망합니다. 캐릭터가 사망했다면, -1을 리턴해주세요.
"""

# 테스트 케이스 1
hp = 200
monsters = {'골렘' : 40 , '리본돼지' : 20 ,'슬라임' : 10} # 골렘 0 , 리본돼지 1, 슬라임 2


# 테스트 케이스
attack =  [-1,0,1,1,0,2,-1,1]        
attack2 = [0,0,0,0,0,2,-1,1]        
attack3 = [-1,-1,1,1,0,2,-1,1]      
attack4 = [-1,-1,-1,-1,-1,-1,-1,-1] 


def solution(hp, monsters, attack):
    monList = list(monsters.values())  # list(변수.values())로 [40, 20, 10] 을 추출
    
    for atk in attack:
        if atk == -1:
            print('ㅋㅋ 좁밥쉑')
            continue  # 회피시  넘어감
        if atk >= 0 and atk < len(monList): # list [40, 20, 10]
            hp -= monList[atk]  # 몬스터 공격 데미지 적용
            print('윽억,ㅇ,,ㅇ겅어거억억')
        
        if hp <= 0:
            print('영웅이 전사했습니다.')
            return 'ㅋㅋ 주것누'
    
    return hp

print(solution(hp,monsters,attack))     # 50
print('-----------------')
print(solution(hp,monsters,attack2))    # -1
print('-----------------')
print(solution(hp,monsters,attack3))    # 90
print('-----------------')
print(solution(hp,monsters,attack4))    # 200