import io
import sys

# input here
_INPUT = """\
3 4
1 1 2 1
2 1 1 2
2 1 1 2
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\

"""

# ------------ your code here ---------------

H, W = map(int, input().split())
B = [list(map(int, input().split())) for i in range(H)]
L = [[0] * W for i in range(H)]
# print(B)
# print(L)

for i in range(H):
    for j in range(W):
        # 一列目
        if i == 0:
            L[i][j] = B[i][j]
            continue

        L[i][j] = L[i-1][j] + B[i][j]
        if j-1 >= 0:
            L[i][j] = max(L[i][j], L[i-1][j-1] + B[i][j])
        if j+1 < W:
            L[i][j] = max(L[i][j], L[i-1][j+1] + B[i][j])

print(max(L[H-1]))