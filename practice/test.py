result = 0

# 切り上げ
a = "A"
b = str(a) # 型変換

# 文字列を並び替える
S = "AtCoder"
S = "".join(sorted(S))
print(S) # "ACdeort"を出力

#こうすることで改行する代わりに空白を入れて一行で出力される
print(result,end=" ")