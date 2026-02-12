T = int(input())
for tc in range(1, T+1):
    # 농장의 크기
    N = int(input())
    # 농작물의 가치 
    value = [list(map(int, input())) for _ in range(N)]

    # 가운데를 의미
    mid = N // 2

    # 수익 변수 설정
    profit = 0

    for i in range(N):
        # i행 j열이 중앙에서 얼마나 멀리 떨어져있는지 계산하기 위한 변수
        distance = abs(i - mid)
        # 그 차이만큼의 개수의 원소를 수익에 더하기 
        for j in range(distance, N - distance): 
            profit += value[i][j]

    print(f'#{tc} {profit}') 