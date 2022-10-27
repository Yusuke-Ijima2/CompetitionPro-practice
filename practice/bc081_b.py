import io
import sys

# input here
_INPUT = """\
3
8 12 40
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
2
"""

# ------------ your code here ---------------

N = int(input())
A = map(int, input().split())

def how_many_times(num):
    counter = 0
    while num % 2 == 0:
        num //= 2
        counter += 1
    return counter 

# 出力するときはmapは一つにする、それかlistにして出力
print(min(map(how_many_times,A)))
# print(map(how_many_times,A))