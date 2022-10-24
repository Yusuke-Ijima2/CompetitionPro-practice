import io
import sys

# input here
_INPUT = """\
1
2 2 2
333
"""
sys.stdin = io.StringIO(_INPUT)

# your code here

var1 = int(input())
print(var1)
# → 1

var2 = map(int, input().split())
print(list(var2))
# → [2, 2, 2]

var3 = list(input())
print(var3)
# → ['3', '3', '3']