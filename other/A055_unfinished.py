import io
import sys

# input here
_INPUT = """\
7 6
######
#....#
#.##.#
#.#S.#
#.####
#.....
######
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
YES
"""

# ------------ your code here ---------------
from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
que = deque()
ok = False

for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            sy, sx = i, j
            ok = True
            break
    if ok:
        break

que.append([sy, sx])

print(que)

while que:
    y, x = que.popleft()

    if y == H-1 or x == W-1 or y == 0 or x == 0:
        print('YES')
        break

    maze[y][x] = '#'
    
    for ny, nx in ([y+1, x], [y-1, x], [y, x+1], [y, x-1]):
        if maze[ny][nx] != '#' and 0 <= ny < H and 0 <= nx < W:
            que.append([ny, nx]) 

else:
    print('NO')