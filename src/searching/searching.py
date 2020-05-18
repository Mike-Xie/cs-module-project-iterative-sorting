def linear_search(items: list, target: int):
    # Your code here
    for i in items:
    	if i == target:
    		# important, this breaks if can't find 
    		return items.index(target) 

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(items: list, target: int):
    # does integer math, find item at halfway point
    left = 0
    right = len(items) - 1

    while left <= right:
    	# find midpoint

    	mid = (left + right) // 2 

    	if items[mid] == target:
    		return mid

    	if items[mid] < target:
    		left = mid + 1

    	else:
    		right = mid - 1 

    return -1 

