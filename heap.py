def heapify(arr):
    for i in xrange(len(arr)/2 - 1, -1, -1):
        try:
            if (arr[i] < arr[2*i + 1]):
                arr[i], arr[2*i + 1] = arr[2*i + 1], arr[i]
            if (arr[i] < arr[2*i + 2]):
                arr[i], arr[2*i + 2] = arr[2*i + 2], arr[i]
        except:
            pass		
    return arr

arr = [9,6,5,2,3,10]
heap = heapify(arr)
print heap