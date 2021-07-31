import sys

def findMinInsertions(str, first, last):
 
    if (first > last):
        return sys.maxsize
    if (first == last):
        return 0
    if (first == last - 1):
        return 0 if(str[first] == str[last]) else 1
     
    if(str[first] == str[last]):
        return findMinInsertions(str, first + 1, last - 1)
    else:
        return (min(findMinInsertions(str, first, last - 1),
                    findMinInsertions(str, first + 1, last)) + 1)

if __name__ == "__main__":
     
    str = input("Enter String: ")
    print(findMinInsertions(str, 0, len(str) - 1))