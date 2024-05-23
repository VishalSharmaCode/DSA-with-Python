def array():
    arr1 = []
    x=int(input("Give the length of an array :"))
    for i in range(x):
        y = int(input("Give the elements of array :"))
        arr1.append(y)
    return arr1
arr = array()

item = int(input("GIve the number which you want to search from the array:"))

for i in range(len(arr)):
    if arr[i]==item:
        # print(i)
        break
if item == arr[i]:
    print(i)
else:
    print('Item is not found')