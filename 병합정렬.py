def merge_sort(start, end):
    global cnt  

    # 원소가 1개면 정렬 끝
    if start == end - 1:
        return start, end
    
    # 가운데 나누기
    mid = (start + end) // 2

    # 왼쪽 정렬
    left_s, left_e = merge_sort(start, mid)
    right_s, right_e = merge_sort(mid, end)

    # 문제 조건: 병합하기 직전에 왼쪽의 마지막 원소가 오른쪽의 마지막 원소보다 크면 카운트
    if arr[left_e - 1] > arr[right_e - 1]:
        cnt += 1
    
    # 병합
    merge(left_s, left_e, right_s, right_e)
    
    return start, end

def merge(left_s, left_e, right_s, right_e):
    # 왼쪽 현재 위치
    l = left_s
    # 오른쪽 현재 위치
    r = right_s

    # 합친 길이 
    size = right_e - left_s

    # 임시 배열
    result = [0] * size

    idx = 0

    # 작은 값부터 result에 넣기
    while l < left_e and r < right_e:
        if arr[l] <= arr[r]:
            result[idx] = arr[l]
            l += 1
        
        else:
            result[idx] = arr[r]
            r += 1
        
        idx += 1

    # 오른쪽이 남은 경우
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1
    
    # 왼쪽이 남은 경우
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1
    
    # 원본 배열에 다시 반영
    for i in range(size):
        arr[left_s + i] = result[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

    merge_sort(0, N)

    print(f'#{tc} {arr[N//2]} {cnt}')
