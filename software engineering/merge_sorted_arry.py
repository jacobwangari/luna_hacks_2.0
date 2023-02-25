import heapq

def merge_sorted_arrays(arr1, arr2):
    #heapq.merge to merge the array
    merged_array = heapq.merge(arr1, arr2)
    #set removes repeated characters
    #list convert the set back to list
    return list(set(merged_array))

arr1 = [1,2,3]
arr2 = [3,4,5]

print(merge_sorted_arrays(arr1,arr2))
