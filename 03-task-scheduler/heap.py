class MaxHeap:
    """Max-heap stored in a list. Items are (priority, name) tuples."""

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def insert(self, priority, name):
        self.items.append((priority, name))
        i = len(self.items) - 1
        # move the new item up while it is bigger than its parent
        while i > 0:
            parent = (i - 1) // 2
            if self.items[i] > self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
                i = parent
            else:
                break

    def extract_max(self):
        if not self.items:
            raise IndexError("heap is empty")
        top = self.items[0]
        last = self.items.pop()
        if self.items:
            self.items[0] = last
            self.max_heapify(0)
        return top

    def max_heapify(self, i):
        n = len(self.items)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and self.items[left] > self.items[largest]:
                largest = left
            if right < n and self.items[right] > self.items[largest]:
                largest = right
            if largest == i:
                break
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            i = largest
