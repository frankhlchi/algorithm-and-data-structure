
def bubblesort(num_list):
    for end_index in range(len(num_list)-1,0,-1):
        sorted = True
        for i in range(end_index):
            if  num_list[i] > num_list[i+1]:
                temp = num_list[i+1]
                num_list[i + 1] = num_list[i]
                num_list[i] = temp
                sorted = False
        if sorted:
            return num_list
    return num_list


def selectionsort (num_list):
    for end_index in range(len(num_list)-1,0,-1):
        max_index = 0
        for loc in range(1,end_index+1):
            if num_list[loc] > num_list[max_index]:
                max_index = loc
        temp =  num_list[end_index]
        num_list[end_index] = num_list[max_index ]
        num_list[max_index] = temp
    return num_list

def mergesort(num_list):
    if len(num_list) <=1 :
        return num_list
    mid = len(num_list)//2
    left = mergesort(num_list[:mid])
    right = mergesort(num_list[mid:])

    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged


def quicksort(num_list):
    return quicksort_helper(num_list,0, len(num_list)-1)

def quicksort_helper(num_list, first, last):
    if first < last:
        splitpoint  = partition(num_list, first, last)
        quicksort_helper(num_list, first,splitpoint -1 )
        quicksort_helper(num_list,  splitpoint + 1,last)
    return num_list

def partition(num_list, first, last):
    pivot = num_list[first]
    left = first +1
    right = last
    done = False
    while not done:
        while left <= right and num_list[left] <= pivot:
            left +=1
        while right >= left and num_list[right] >= pivot:
            right -=1
        if right < left:
            done = True
        else:
            temp = num_list[left]
            num_list[left] = num_list[right]
            num_list[right] = temp
    temp = num_list[first]
    num_list[first] = num_list[right]
    num_list[right] =temp
    return right



alist = [54,26,93,17,77,31,44,55,20]
print('bubble sort',bubblesort(alist))
print('selection sort',bubblesort(alist))
print('merge sort',mergesort(alist))
print('quick sort',quicksort(alist))