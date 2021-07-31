from math import ceil

def candyStore(array,size,free):
    array.sort()
    resultant = int(ceil(size/free))
    return  sum(array[:resultant]), sum(array[-resultant:])
    
size = int(input("Enter array size : "))
array = []
for item in range(0, size):
    element = int(input("Enter array element: "))
    array.append(element)

free = int(input("Enter value for K: "))
 
print(candyStore(array,size,free))
