import io
import sys

# input here
_INPUT = """\
3 4
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
Even
"""

# ------------ your code here ---------------

a,b = list(map(int, input().split()))

if a*b%2 == 0:
    print("Even")
else:
    print("Odd")