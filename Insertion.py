def array():
    arr1 = []
    x=int(input("Give the length of an array :"))# length of an array given by an user
    for i in range(x):
        y = int(input("Give the elements of array :")) # elements in an array
        arr1.append(y)
    return arr1
arr = array() # array which is given by user 
item = int(input("Give the item which you want to add :")) # Item which you want to Insert
loc = int(input('Give the location where you want to add the number :')) # Location where you want to insert the element 

arr1 = [0]*(len(arr)+1) # Make a duplicate array with +1 length

for i in range(len(arr)):
    arr1[i] = arr[i]
for i in range(loc, len(arr)):
    arr1[i+1] = arr[i]
arr1[loc] = item
arr[:] = arr1
print(arr)


