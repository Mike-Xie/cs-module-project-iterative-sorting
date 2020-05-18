# TO-DO: Complete the selection_sort() function below
def selection_sort(items: list):
    # loop through n-1 elements
    for i in range(0, len(items) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # for the items left to loop thru
        # if any of those are smaller, assign to smallest index
        # and then increment cur_index by 1
        for j in range(cur_index + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j
        # swap item in current index with smallest index 
        # has to be done same time         
        items[smallest_index], items[cur_index] = items[cur_index], items[smallest_index]
    

    return items 

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(items: list):
    # for all the items
    for i in range(0, len(items) - 1):
        # for items left over to loop thru
        # because decrement end of list by one each time
        for j in range(0, len(items) - i -1):
            if items[j] > items[j+1]:

                items[j], items[j+1] = items[j+1], items[j]


    return items


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
