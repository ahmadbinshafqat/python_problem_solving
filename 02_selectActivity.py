def activitySelection(start , end ):
    end_array_len = len(end)
    final_list = []
    
    first = 0
    final_list.append(first)
    print (first),
 
    for second in range(end_array_len):
        if start[second] >= end[first]:
            final_list.append(second)
            print (second),
            first = second
    return final_list
start = []
 
start_array_size = int(input("Enter size for start array : "))
 
for item in range(0, start_array_size):
    element = int(input("Enter element in start_array: "))
 
    start.append(element) # adding the element

end = []
 
end_array_size = int(input("Enter size for end array : "))
 
for item in range(0, end_array_size):
    element = int(input("Enter element in end_array: "))
 
    end.append(element) # adding the element
     
#start = [1 , 3 , 0 , 5 , 8 , 5]
#end = [2 , 4 , 6 , 7 , 9 , 9]
print(activitySelection(start , end))