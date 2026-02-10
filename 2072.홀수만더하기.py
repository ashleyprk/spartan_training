T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))

    # 모두 0 또는 양수이므로 총합 최소가 0
    total = 0

    for i in N:
        if i % 2 == 1:
            total += i 
    
    print(f'#{tc} {total}')
