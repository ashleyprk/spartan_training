T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cntry = [list(input()) for _ in range(N)]

    result = float('inf')

    # 흰 줄의 개수 w, 파란색 줄의 개수 b, 빨간색 줄의 개수: r
    for w in range(1, N - 1):
        for b in range(1, N - w):
            r = N - w - b
            if r < 1:
                continue


            # 새로운 방문 배열을 만들어서 
            # 해당 컬러가 올바른 위치에 있지 않을때를 표시하게 설정
            visited = [[0] * M for _ in range(N)]

            # 해당 컬러가 올바른 위치에 있지 않을때 방문 표시
            # 맨 위가 하얀색
            for i in range(w):
                for j in range(M):
                    if cntry[i][j] != 'W':
                        visited[i][j] = 1

            # 다음 줄이 파란색
            for i in range(w, w + b):
                for j in range(M):
                    if cntry[i][j] != 'B':
                        visited[i][j] = 1

            # 나머지가 빨간색
            for i in range(w + b, N):
                for j in range(M):
                    if cntry[i][j] != 'R':
                        visited[i][j] = 1

            # 방문 배열에서 1로 표시된 것의 개수가 정답 
            # 다시 칠해야 하는 칸 수가 방문 배열에서 1로 표시된 칸
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if visited[i][j] == 1:
                        cnt += 1
            
            result = min(result, cnt) 
    
    print(f'#{tc} {result}') 

    
