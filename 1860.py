# 그리디 + 정렬
# 손님이 도착한 시간 t까지 만들어진 붕어빵 개수 = t/M * K

# N: 사람 수, M: 붕어빵을 만들 수 있는 시간, K: 붕어빵의 개수
# 기다리는 시간 없이 붕어빵 제공 가능 / 불가능 여부 판별

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arriv = list(map(int, input().split()))

    # 일찍 도착한 순으로 정렬 !!
    arriv.sort() 

    possible = True

    # 그 시간까지 만든 붕어빵 개수 >= 그때까지 온 손님 수 를 확인 

    # i번째 손님을 확인
    # 몇 초에 도착했는지 확인
    for i in range(N):
        t = arriv[i]

        # t 초까지 만들어진 붕어빵 개수
        bread = (t // M) * K

        # i번째 손님까지 i+1명이 필요
        # 지금까지 만든 붕어빵이 지금까지 온 손님보다 부족한가? 
        # (만든 붕어빵 < 지금까지 온 손님) == 붕어빵이 부족하다
        if bread < (i + 1):
            possible = False
            break
    
    if possible:
        print(f'#{tc} Possible')
    
    else:
        print(f'#{tc} Impossible')