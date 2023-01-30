str1 = input('一つ目の文字列：')
str2 = input('二つ目の文字列：')

str1 += ' '
n = min([len(str1), len(str2)])

for i in range(n):
    if str1[-n+i-1:-1] == str2[0:n-i]:
        print('共通部分は ’', str1[-n+i-1:-1], '’')
        break
    else:
        if len(str2[0:n-i]) == 1:
            print('共通部分は存在しません')
