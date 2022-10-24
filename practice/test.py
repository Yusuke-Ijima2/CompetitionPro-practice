import io
import sys

# input here
_INPUT = """\
10 6
"""
sys.stdin = io.StringIO(_INPUT)

# ------------ your code here ---------------

H,A = map(int, input().split())

if H % A == 0 :
    print(H//A)
else:
    print(H//A +1)

# 切り上げ

for i in range(10, 20):
    print(++i)
