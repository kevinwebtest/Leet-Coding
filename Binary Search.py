# TOOK FROM GEEKSFORGEEKS.ORG
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1

	while low <= high:

		mid = (high + low) // 2

		if arr[mid] < x:  # If x is greater, ignore left half
			low = mid + 1

		elif arr[mid] > x:  # If x is smaller, ignore right half
			high = mid - 1
      
		else:  # means x is present at mid
			return mid
	# If we reach here, then the element was not present
	return -1

# Test array
arr = [ 1,2,3,4,5,6,9 ]
x = 6

# Function call
result = binary_search(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
