def array():
    arr1 = []
    x = int(input("Give the leangth of the array :"))
    for i in range(x):
        y = int(input("Give the elements :"))
        arr1.append(y)
    return arr1
arr = array()
arr.sort()
item = int(input("Give the element which you want to search in array :"))
begning = 0
end = len(arr)
mid = (begning+end)//2

while begning<=end & arr[mid] != item:
    if item <arr[mid]:
        end = mid-1
    else:
        begning = mid+1
    mid = (begning+end)//2
if arr[mid] == item:
    print(mid)
else:
    print('Item is not Found')
