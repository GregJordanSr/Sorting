# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

print(selection_sort([436, 89, 3042, 8143, 4, 1, 76, 632, 233, 9]))

# ---------------------------------------------------------------


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    switch_places = True

    while switch_places:
        switch_places = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            switch_places = True 
    return arr
print(bubble_sort([596, 819, 782, 5143, 8, 5, 176, 632, 333, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr