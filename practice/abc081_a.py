import io
import sys

# input here
_INPUT = """\
101
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
2
"""

# ------------ your code here ---------------

a = list(map(int,input()))
counter=0
# print(a)

for i in range(len(a)):
    # print(i)
    if a[i]==1:
        counter+=1

print(counter)