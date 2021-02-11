# p.118 구현 - 게임 개발
import sys
input = sys.stdin.readline

LAND = 0
SEA = 1
VISITED = 2

dir = [0, 3, 2, 1]  # 북, 서, 남, 동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
y, x, d = map(int, input().split())
mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))

is_stopped = False  # 멈췄는지 여부
mat[y][x] = VISITED  # 첫째 칸 방문
ans = 1  # 방문한 칸 수

while not is_stopped:
    for i in range(1, 5):
        # 왼쪽 방향으로 회전
        next_dir_idx = dir[(d + i) % 4]

        # 방문을 시도할 새로운 좌표
        nx, ny = x + dx[next_dir_idx], y + dy[next_dir_idx]

        # 해당 방향이 바다거나 방문한 곳이라면, 앞으로 움직이지 않는다
        if mat[ny][nx] == SEA or mat[ny][nx] == VISITED:
            # 한 바퀴 모두 돌았다면 바라본 방향을 유지한 채로 뒤로 간다
            if i >= 4:
                # 뒤로 이동한 좌표 임시 저장
                nx, ny = x - dx[next_dir_idx], y - dy[next_dir_idx]

                if mat[ny][nx] == SEA:
                    # 뒤가 바다라면 종료
                    is_stopped = True
                    break
                else:
                    # 좌표 및 방향 저장한 채 뒤로 일보 후퇴
                    x, y = nx, ny
                    d = next_dir_idx
                    break

            continue
        else:
            # 해당 방향이 방문한 적 없는 육지라면, 해당 방향으로 전진
            x, y = nx, ny
            d = next_dir_idx

            mat[y][x] = VISITED
            ans += 1
            break

print(ans)
