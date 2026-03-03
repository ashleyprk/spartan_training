# NxN행렬
# 0: 통로, 1: 벽:, 2: 술래
# 감시를 피하기 위해서는 술래와 인접한 정점이 아니어야 함
# 감시를 피할 수 없는 칸을 위험한 칸이라고 두어야 함
# 술래와 인접한 영역 탐색하기 위해서는 벽이 아니어야하고, 범위 안에 있어야한다

T = int(input())
for tc in range(1, T +1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 술래 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:


                # 현재 술래의 위치에서 방향 탐색
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:

                    # 이동할 칸 수 설정
                    c = 1
                    while True: 
                        # 인접한 점 설정
                        ni, nj = i + di * c, j + dj * c

                        # 이 점이 범위 밖에 있으면 탐색 중단
                        if not (0 <= ni < N and 0 <= nj < N):
                            break

                        # 이 점이 벽을 만나면 탐색 중단
                        if arr[ni][nj] == 1:
                            break

                        # 이 점이 통로이면 위험한 칸 설정
                        # 9라고 설정
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = 9

                        c += 1
    
    # 감시를 피할 수 있는 칸 순회
    
    # 감시를 피할 수 있는 칸 설정 
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    
    print(f'#{tc} {cnt}')
                    