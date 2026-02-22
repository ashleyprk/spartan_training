T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # N개의 돌 상태 0 = 흰, 1 = 검 또는 0 = 검, 1 = 흰
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        # 입력 i는 1번부터 시작하므로 인덱스(0번부터)로 바꿔줌
        start = i - 1

        # i 번째 돌의 현재 색을 기준 색으로 잡음
        color = stones[start]

        # 뒤집기할 마지막 인덱스를 계산
        end = start + j - 1

        # 돌은 N개까지만 있으니 end가 N-1을 넘어가면 N-1로 잘라야함
        if end >= N:
            end = N - 1
        
        # 시작부터 끝까지 모두 i번째 돌의 색으로 바꿈
        for k in range(start, end + 1):
            stones[k] = color
    
    print(f'#{tc}', *stones)