s = "H1:V2"
ans = []
def solution(s):
    column = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    line = [1,2,3,4,5,6,7,8,9]
    cell_alp_1 = s[0]
    cell_num_1 = int(s[1])
    cell_alp_2 = s[3]
    cell_num_2 = int(s[4])
    
    if cell_alp_1 == cell_alp_2:
        ans_num_list = line[cell_num_1 - 1 : cell_num_2]
        ans_str_list = [str(i) for i in ans_num_list]
        ans_arr = []
        for a in ans_str_list:
            ans_arr.append(cell_alp_1 + a)
        print(ans_arr)
    else:
        ans_num_list = line[cell_num_1 - 1 : cell_num_2]
        ans_str_list = [str(i) for i in ans_num_list]
        ans_alp_list = column[column.index(cell_alp_1) : column.index(cell_alp_2) + 1]
        ans_arr = []
        for i in ans_alp_list:
            for j in ans_str_list:
                ans_arr.append(i + j)
        print(ans_arr)
        

solution(s)