# [입력]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 항상 B가 더 길게 만들기 (짧은 걸 A로)
    if N > M:
        A, B = B, A
        N, M = M, N
    
    # 합의 최댓값 변수설정
    max_v = -float('inf')

    # A < B
    # A = 4, B = 5: 5-4+1 까지
    # A = 4, B = 6: 6-4+1 까지
    for j in range(M-N+1):
        total = 0 # 위치마다 초기화 
        for i in range(N):
            total += A[i]*B[j+i]

        if max_v < total:
            max_v = total

    # [출력]
    print(f'#{tc} {max_v}')