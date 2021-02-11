# p.118 구현 - 게임 개발
import timeit
# ======================================== #
import sys
input = sys.stdin.readline

LAND = 0
SEA = 1
VISITED = 2

dir_str = ['북', '서', '남', '동']
dir = [0, 3, 2, 1]  # 북, 서, 남, 동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
y, x, d = map(int, input().split())
mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))

# ======================================== #
start_time = timeit.default_timer()
# ======================================== #

is_stopped = False  # 멈췄는지 여부
mat[y][x] = VISITED # 첫째 칸 방문
ans = 1             # 방문한 칸 수

while not is_stopped:
    print('====================')
    for row in mat:
        print(row)
    
    print('Currently: (%d, %d), Looking: %s쪽' % (x, y, dir_str[d]))
    print('Visited: %d block(s)' % ans)

    for i in range(1, 5):    
        # 왼쪽 방향으로 회전
        next_dir_idx = dir[(d + i) % 4]
        print('Turning left, Looking: %s쪽' % dir_str[next_dir_idx])

        # 방문을 시도할 새로운 좌표
        nx, ny = x + dx[next_dir_idx], y + dy[next_dir_idx]
        
        # 해당 방향이 바다거나 방문한 곳이라면, 앞으로 움직이지 않는다
        if mat[ny][nx] == SEA or mat[ny][nx] == VISITED:
            # 한 바퀴 모두 돌았다면 바라본 방향을 유지한 채로 뒤로 간다
            if i >= 4:
                print('[뒤로 후퇴 시도]')

                # 뒤로 이동한 좌표 임시 저장
                nx, ny = x - dx[next_dir_idx], y - dy[next_dir_idx]

                if mat[ny][nx] == SEA:
                    # 뒤가 바다라면 종료
                    print('뒤는 바다입니다. 종료!')
                    is_stopped = True
                    break
                else:
                    # 좌표 및 방향 저장한 채 뒤로 일보 후퇴
                    x, y = nx, ny
                    d = next_dir_idx
                    print('방향 유지, 뒤로 일보 후퇴. Now: (%d, %d), Looking: %s쪽' % (x, y, dir_str[d]))
                    break

            continue
        else:
            # 해당 방향이 방문한 적 없는 육지라면, 해당 방향으로 전진
            x, y = nx, ny
            d = next_dir_idx

            mat[y][x] = VISITED
            ans += 1

            print('앞으로 전진. Now: (%d, %d), Looking: %s쪽' % (x, y, dir_str[d]))
            break

print(ans)

# ======================================== #
end_time = timeit.default_timer()
exec_time = end_time - start_time
print('Total execution time: %fs' % exec_time)
# ======================================== #
"""
Test cases

4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

5 5
1 1 0
1 1 1 1 1
1 0 0 1 1
1 1 0 1 1
1 1 0 1 1
1 1 1 1 1

6 6
2 2 3
1 1 1 1 1 1
1 0 0 1 0 1
1 0 0 0 0 1
1 1 0 1 1 1
1 0 0 1 0 1
1 1 1 1 1 1
"""
