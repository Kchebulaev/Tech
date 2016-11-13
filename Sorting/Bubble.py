import random


def bubbleSort(array, end=1):
    if end == 1:
        return array
    for i in range(0, end -1):
        if array[i] > array[i+1]:
            tmp = array[i+1]
            array[i+1] = array[i]
            array[i] = tmp
    return  bubbleSort(array, end -1)

arr = []
for i in range(0, random.randint(1, 100)):
    arr.append(random.randint(0,100))

print arr
print "========"
print bubbleSort(arr, len(arr))
