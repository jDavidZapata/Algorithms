// Linear Search

/*

Time Complexity: O(n)
Space Complexity: O(1)

LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index
*/

#include <stdio.h>
#include <stdlib.h>

int linearSearch(int array[], int n, int key)
{
  for (int i = 0; i < n; i++)
    if (array[i] == key)
      return i;
  return -1;
}

int main()
{
  int array[] = {2, 4, 60, 8, 3, 5, 1};
  int x = 3;
  int n = sizeof(array) / sizeof(array[0]);

  int result = search(array, n, x);

  (result == -1) ? printf("Element not found.") : printf("Element found at index: %d\nElement is = %d", result, array[result]);
}
