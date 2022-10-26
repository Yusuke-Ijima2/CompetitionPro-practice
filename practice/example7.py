import io
import sys

# input here
_INPUT = """\
3
2 7 4
"""
sys.stdin = io.StringIO(_INPUT)

# ------------ your code here ---------------

N = int(input())
a = list(map(int, input().split()))

# 大きい順にソート
a.sort(reverse=True)

result = 0

# 配列aの各要素を交互に足し引きしていく
for i in range(N):
    if i % 2 == 0: # 0%2==0だから
        result += a[i]
    else:
        result -= a[i]