T = int(input())  # 테스트 케이스 개수 입력

# 각 테스트 케이스 반복
for tc in range(1, T + 1):

    N = int(input())      # 농장 크기 입력 (항상 홀수)
    M = N // 2            # 중앙 인덱스 (다이아몬드의 중심 행)
    ans = 0               # 수익 합을 저장할 변수

    # N개의 행을 차례대로 처리
    for i in range(N):
        row = input()

        # 현재 행이 중앙에서 얼마나 떨어져 있는지 계산
        dist = abs(i - M)

        # 다이아몬드 모양의 열 범위 설정
        # 시작 열: dist
        for j in range(dist, N - dist):

            # row[j]는 문자이므로 int로 변환해서 더함
            ans += int(row[j])

    print(f'#{tc} {ans}')
