# p.96 그리디 - 숫자 카드 게임
import sys
input = sys.stdin.readline

# 각 행마다 최솟값을 담는 배열
arr = []

# N: #rows, M: #cols
N, M = map(int, input().split())

# 각 행마다 최솟값 담기
for i in range(N):
    arr.append(min(list(map(int, input().split()))))

# 최솟값 중 최댓값 출력
print(max(arr))

# ========================================
# 코드 더 줄여보기
# ========================================
# import sys
# input = sys.stdin.readline

# # N: #rows, M: #cols
# N, M = map(int, input().split())

# # 각 행마다 최솟값 저장
# arr = [min(list(map(int, input().split()))) for i in range(N)]

# # 최솟값 중 최댓값 출력
# print(max(arr))
# ========================================

# ========================================
# 코드 더더욱 줄여보기
# ========================================
# import sys
# input = sys.stdin.readline

# # 최솟값 중 최댓값 출력
# print(max([min(list(map(int, input().split()))) for i in range(list(map(int, input().split()))[0])]))
# ========================================
