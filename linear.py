def array():
    arr1 = []
    x = int(input("Give the leangth of the array :"))
    for i in range(x):
        y = int(input("Give the elements :"))
        arr1.append(y)
    return arr1
arr = array()
item = int(input("Give the element which you want to search in array :"))
for i in range(len(arr)):
    if item == arr[i]:
        break
if item == arr[i]:
    print(i)
else:
    print("Item is not found in the array")