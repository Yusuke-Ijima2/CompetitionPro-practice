import io
import sys
from itertools import combinations

# input here
_INPUT = """\
thirty
tycoon
aiueo
pow
"""
sys.stdin = io.StringIO(_INPUT)

str = []

while True:
    try:
        str.append(input())
    except:
        break


patterns = list(combinations(str, 2))

max_length = 0
for pattern in patterns:
    str1 = pattern[0]
    str2 = pattern[1]

    str1 += ' '
    n = min([len(str1), len(str2)])

    for i in range(n):
        if str1[-n+i-1:-1] == str2[0:n-i]:
            # print('共通部分は ’', str1[-n+i-1:-1], '’')
            if max_length <= len(str1[-n+i-1:-1]):
                max_length = len(str1[-n+i-1:-1])
            break
        else:
            pass
            # if len(str2[0:n-i]) == 1:
            #     print('共通部分は存在しません')
        
print(max_length)