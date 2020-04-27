# Linear Search in Python

"""

LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index

Time Complexity: O(n)

Space Complexity: O(1)

"""

def linearSearch(array, n, key):

    for i in range(0, n):
        if (array[i] == key):
            return i
    return -1


array = [7, 9, 11, 55, 13, 3, 0, 49]
x = 13
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element is: ", array[result])
    print("Element found at index: ", result)
