from Heap.MyMaxHeap import MyMaxHeap

print("Chương trình - Binary Max-Heap - thêm/bớt phần tử !")


def is_max_heap(arr, index, length):
    left = index * 2 + 1
    right = left + 1
    if left < length and arr[index] < arr[left]:
        return False
    if right < length and arr[index] < arr[right]:
        return False

    left_ok = left > length - 1 or is_max_heap(arr, left, length)
    if not left_ok:
        return False

    right_ok = right > length - 1 or is_max_heap(arr, right, length)
    return right_ok


array = [1, 5, 3, 7, 9, 8]
if is_max_heap(array, 0, len(array)):
    print('array is a binary max-heap')
else:
    print('array is NOT a binary max-heap')

max_heap = MyMaxHeap()
max_heap.set(array)
# for i in array:
#     max_heap.add(i)
max_heap.print()

if is_max_heap(max_heap.get(), 0, len(max_heap.get())):
    print('array is a binary max-heap')
else:
    print('array is NOT a binary max-heap')

max_heap.build()
if is_max_heap(max_heap.get(), 0, len(max_heap.get())):
    print('array is a binary max-heap')
else:
    print('array is NOT a binary max-heap')
max_heap.print()

while max_heap.size > 0:
    print(max_heap.remove(), end=' ')
    # max_heap.print()
    # if is_max_heap(max_heap.get(), 0, len(max_heap.get())):
    #     print('array is a binary max-heap')
    # else:
    #     print('array is NOT a binary max-heap')
