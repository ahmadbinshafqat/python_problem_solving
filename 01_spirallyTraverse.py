def spirallyTraverse(end_row, end_col, array):
    start_row = 0
    start_col = 0
    
    final_result_list = []
    
    while (start_row < end_row and start_col < end_col):
        for index in range(start_col, end_col):
            final_result_list.append(array[start_row][index])
 
        start_row += 1
 
        for index in range(start_row, end_row):
            final_result_list.append(array[index][end_col - 1])
            
        end_col -= 1
 
        if (start_row < end_row):
 
            for index in range(end_col - 1, (start_col - 1), -1):
                final_result_list.append(array[end_row - 1][index])
                
            end_row -= 1
 
        if (start_col < end_col):
            for index in range(end_row - 1, start_row - 1, -1):
                final_result_list.append(array[index][start_col])
                
            start_col += 1
            
    return final_result_list
 
array = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18],
     [19, 20, 21, 22, 23, 24]]
 
R = input("Enter Row: ")
C = input("Enter Column: ")

print(spirallyTraverse(int(R), int(C), array))