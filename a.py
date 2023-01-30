# intervals = [[2,4],[1,2],[4,6]]

# def solution(intervals):
#     print(intervals)
#     start =[]
#     for i in range(len(intervals)):
#         start.append(intervals[i][0])
#     for j in range(len(intervals)):
#         intervals[j] = start[i]
    




# solution(intervals)

word_list = [
"thirty",
"tycoon"]
print(word_list[0] in word_list[1])
for i in range(len(word_list)-1):
        print(i)
        if word_list[i] in word_list[i+1]:
            print("test")