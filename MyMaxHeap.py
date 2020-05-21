class MyMaxHeap:
    __size = 0
    __data = []

    # def __init__(self):
        # print("MyMaxHeap constructor")

    @property
    def size(self):
        return self.__size

    def get(self):
        return self.__data

    def set(self, data):
        self.__data = data
        self.__size = len(self.__data)

    def print(self):
        print(self.__data)

    def add(self, item):
        self.__size += 1
        self.__data.append(item)
        current = self.__size - 1
        while True:
            parent = (current - 1) // 2
            if parent < 0:
                break
            if self.__data[current] > self.__data[parent]:
                temp = self.__data[parent]
                self.__data[parent] = self.__data[current]
                self.__data[current] = temp
                current = parent
            else:
                break

    def remove(self):
        if self.__size > 0:
            self.__size -= 1
            value = self.__data[0]
            self.__data[0] = self.__data[self.__size]
            self.__data.pop()
            current = 0
            while True:
                left = current * 2 + 1
                right = left + 1
                largest = current
                if left < self.__size and self.__data[left] > self.__data[current]:
                    largest = left
                if right < self.__size and self.__data[right] > self.__data[largest]:
                    largest = right
                if largest == current:
                    break
                temp = self.__data[largest]
                self.__data[largest] = self.__data[current]
                self.__data[current] = temp
                current = largest
            return value
        else:
            return None

    def heapify(self, current):
        left = current * 2 + 1
        right = left + 1
        largest = current
        if left < self.__size and self.__data[left] > self.__data[current]:
            largest = left
        if right < self.__size and self.__data[right] > self.__data[largest]:
            largest = right
        if largest == current:
            return
        temp = self.__data[largest]
        self.__data[largest] = self.__data[current]
        self.__data[current] = temp
        self.heapify(largest)

    def build(self):
        for i in range((self.__size - 2) // 2, -1, -1):
            self.heapify(i)
