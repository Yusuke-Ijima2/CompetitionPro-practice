import io
import sys

# input here
_INPUT = """\
2
2
2
100
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
2
"""

# ------------ your code here ---------------

A = int(input()) # 500yen
B = int(input()) # 100yen
C = int(input()) # 50yen
X = int(input()) # ちょうどX yen

counter = 0
for i in range(A+1): # 0の場合も含むため+1
    for j in range(B+1):
        for k in range(C+1):
            if 500*i + 100*j + 50*k == X :
                counter += 1

print(counter)