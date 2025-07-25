
def linearSearch(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i 
    return -1 
def binarySearch(list, value):
    low=0
    high=len(list)-1

    while(high>=low):
        mid=(low+high)//2
        if list[mid]==value:
            return mid
        elif list[mid]>value:
            high=mid-1
        else:
            low=mid+1
    return -1
arr = [1, 3, 5, 7, 9, 11]
target = 11

result = binarySearch(arr, target)
if result!=-1:
    print("vị trí tìm đc là:",result)
else:
    print("ko tim thấy")