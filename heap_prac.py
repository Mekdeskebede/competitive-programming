def heappush(heap,value):
    heap.append(value)
    current = len(heap) - 1
    heapify_up(heap,current)
def heapify_up(heap,current):
    #write your code

    while current > 0:
        if heap[current] < heap[(current-1)//2]:
            heap[current] , heap[(current-1)//2] = heap[(current-1)//2], heap[current]
            current = (current-1)//2
        else:
            break

def test():
    heap = [2, 4, 5, 7, 9, 10]
    heappush(heap, 3)
    assert heap == [2, 4, 3, 7, 9, 10, 5], f"Error: expected [2, 4, 3, 7, 9, 10, 5], but got {heap}"

    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heappush(heap, 0)
    assert heap == [0, 1, 3, 4, 2, 6, 7, 8, 9, 5], f"Error: expected [0, 2, 1, 4, 5, 6, 7, 8, 9, 3], but got {heap}"
   
    print("Great Job !!!")
test()

def heappop(heap):
    if not heap:
        return None
    min_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    current = 0
    heapify_down(heap,len(heap),current)
    return min_value

def heapify_down(arr, n, current):
    index = current*2 + 1
    if index < n:
        left = index
    else:
        return
    if index + 1 < n:
        right = index = 1
    else:
        right = None
        
    if index + 1 < n and arr[index] > arr[index+1]:
        minimum = index+1


    #write your code
