import sys, copy
from collections import deque
input = sys.stdin.readline

vec = ((1,0),(-1,0),(0,1),(0,-1))

def bfs(x, y):
    for dx, dy in vec:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < m and 0 <= ny < n): continue
        if C[ny][nx]: continue
        d.append([nx, ny])
        C[ny][nx] = 2

n, m = map(int, input().split())
M = [list(map(int, input().split())) for _ in ' '*n]
virus = []
for iidx, i in enumerate(M):
    for jidx, j in enumerate(i):
        if j == 2: virus.append([jidx, iidx])

bc = []
for iidx in range(0, n*m):
    if M[iidx//m][iidx%m]: continue
    for jidx in range(iidx+1, n*m):
        if M[jidx//m][jidx%m]: continue
        for kidx in range(jidx+1, n*m):
            if M[kidx//m][kidx%m]: continue
            bc.append([iidx, jidx, kidx])

ans = 0
while bc:
    i, j, k = bc.pop()
    C = copy.deepcopy(M)
    C[i//m][i%m] = C[j//m][j%m] = C[k//m][k%m] = 1
    for x, y in virus:
        d = deque([[x, y]])
        while d:
            x, y = d.popleft()
            bfs(x, y)
    cnt = 0
    for x in C:
        for y in x:
            cnt += 1 if y == 0 else 0
    ans = max(ans, cnt)
print(ans)

