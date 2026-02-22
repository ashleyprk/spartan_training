T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        # 기준 돌 인덱스 0번부터
        center = i - 1

        # center를 기준으로 좌우로 1칸, 2칸, ... j칸까지 확인
        for d in range(1, j + 1):
            left = center - d
            right = center + d

            # 범위를 벗어나면 뒤집기 중지
            if left < 0 or right >= N:
                break

            # 마주보는 두 돌 색이 같으면 둘 다 뒤집기
            if stones[left] == stones[right]:
                if stones[left] == 0:
                    stones[left] = 1
                    stones[right] = 1
                else:
                    stones[left] = 0
                    stones[right] = 0
    
    print(f'#{tc}', *stones)