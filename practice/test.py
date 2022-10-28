result = 0

# 切り上げ
a = "A"
b = str(a) # 型変換

# 文字列を並び替える
S = "AtCoder"
S = "".join(sorted(S))
# print(S) # "ACdeort"を出力

#こうすることで改行する代わりに空白を入れて一行で出力される
# print(result,end=" ")

#  二進法展開
def bit_count(N):
    sum_digit = 0
    while N > 0:
        sum_digit += N % 2
        N //= 2
        print(sum_digit)
    return sum_digit

# print(bit_count(10))
bit_count(10)


[1,3,2,5,4]
5
1
3
2
5
4