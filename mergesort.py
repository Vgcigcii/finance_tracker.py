def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half  = arr[mid:]
    # now the recursion occurs
    left_half = merge_sort(left_half)
    right_half  = merge_sort(right_half)
    return merge(left_half,right_half)
def merge(left,right):
    new = []
    i,j = 0,0
    while i < len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
arr = [1,2,4,6,3,4,9]
print(merge_sort(arr))

