def qsort(arr):
    if not arr:
        return []
    else:
        pivot = arr[0]
        less = [data for data in arr if data < pivot]
        more = [data for data in arr[1:] if x >= pivot]
        sorted_arr = qsort(less) + [pivot] + qsort(more)
        return sorted_arr