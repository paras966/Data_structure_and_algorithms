def isSorted(arr):
    if(len(arr)==0 or len(arr)==1):
        return True
    if(arr[0]>arr[1]):
        return False
    return isSorted(arr[1:])
    
print(isSorted([10,23,23,24,25,26,26,2277]))