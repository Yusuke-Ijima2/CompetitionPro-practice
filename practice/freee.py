import io
import sys

# input here
_INPUT = """\
1
2 2 2
333
4 5
test
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\

"""

# ------------ your code here ---------------

A = int(input())
# print(A) → 1
B = list(map(int, input().split()))
# print(list(B)) → [2, 2, 2]
C = list(input())
# print(C) → ['3', '3', '3']
D,E = list(map(int, input().split()))
# print(D)→ 4
# print(E)→ 5
F = input()
# print(F)→ test

print(A,B,C,D,E,F)

s =[]
for i in range(N):
    a = int(input())
    s.append(a)