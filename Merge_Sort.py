def merge_sort(unsorted_list):
    if len(unsorted_list) <=1:
        return unsorted_list

    mid = len(unsorted_list)//2
    leftList = merge_sort(unsorted_list[:mid]) #recursive
    rightList = merge_sort(unsorted_list[mid:]) #recursive
    return merge(leftList,rightList)

def merge(left,right):
    result=[]
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

length = int(input())
li = [int(input()) for i in range(length)]
print(merge_sort(li))
