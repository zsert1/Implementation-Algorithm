H, W = map(int, input().split())
blocks = list(map(int, input().split()))
answer = 0
#  현재 세로줄에 물이 몇 블럭 채워질 수 있는지
# 특정 위치에 물이 고이기 위해선 자신보다 더 높은 블록으로 왼쪽과 오른쪽이 둘러싸여야함
# 물이 고이는 양은 왼쪽과 오른쪽 블록 중 더 낮은 블록과 현 위치의 값
# 높이가 1인 구역을 왼쪽 오른쪽으로 각각 3, 4 높이의 블록이 감싸고 있다면
# 해당 구역은 더 낮은 블록인 3에서 현 위치의 높이인 1을 뺀 2 만큼의 물이 고인다.
# 첫칸과 마지막 칸은 물이 고일 수 없기 때문에 둔다
for i in range(1, W - 1):
    # 현재 위치의 왼쪽
    left = max(blocks[:i])
    # 현재 위치의 오른쪽
    right = max(blocks[i + 1 :])
    # 더 낮은 블록 기준으로 물이 쌓인다.
    m = min(left, right)
    #  현재 위치가 더 낮을때 더함
    #  현재 높이에서 좌우 중 더 낮은 곳에 빼준다.
    if blocks[i] < m:
        answer += m - blocks[i]
print(answer)
