# p.180 정렬 - 성적이 낮은 순서로 학생 출력하기
"""
2
홍길동 95
이순신 77

5
임꺽정 100
이순신 77
가야금 32
홍길동 95
마리오 66
"""
import sys
input = sys.stdin.readline

N = int(input())
students = []
for i in range(N):
    name, score = input().strip().split()
    students.append((name, int(score)))

ans = [x[0] for x in sorted(students, key=lambda s: s[1])]

for name in ans:
    print(name, end=' ')
