def array():
    arr1 = []
    x=int(input("Give the length of an array :"))
    for i in range(x):
        y = int(input("Give the elements of array :"))
        arr1.append(y)
    return arr1
arr = array()

item = int(input('Give the element which you want to delet from the array :'))
for i in range(len(arr)):
    if arr[i] == item:
        arr.remove(item)
        break
if arr[i] == item:
    arr.remove(item)
    print(arr)
else:
    print("Item is not found in the array")
