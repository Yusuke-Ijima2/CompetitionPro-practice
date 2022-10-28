import io
import sys

# input here
_INPUT = """\
3
1
3
2
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\

"""

# ------------ your code here ---------------

num = int(input())

data = []
for i in range(num):
    data.append(int(input()))

print(data)

count = 0
while len(data) > 0:
    min_num = min(data)
    data.remove(min_num)
    for d in data:
        # print(d)
        if min_num == d - 1:
            data.remove(d)
    count += 1

print(count)
