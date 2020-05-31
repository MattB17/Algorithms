#python3


class Node():
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class StackLL():
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.empty():
            raise ValueError()
        node = self.head
        self.head = node.next
        return node.key

    def see_top(self):
        if self.empty():
            raise ValueError()
        return self.head.key


class StackWithMax():
    def __init__(self):
        self._values_stack = StackLL()
        self._max_stack = StackLL()

    def empty(self):
        return self._values_stack.empty()

    def push(self, key):
        self._values_stack.push(key)
        if ((self._max_stack.empty()) or
            (key >= self._max_stack.see_top())):
            self._max_stack.push(key)

    def pop(self):
        key = self._values_stack.pop()
        if key == self._max_stack.see_top():
            self._max_stack.pop()
        return key

    def max(self):
        return self._max_stack.see_top()


class MaxQueue():
    def __init__(self):
        self._stack1 = StackWithMax()
        self._stack2 = StackWithMax()

    def enqueue(self, key):
        self._stack1.push(key)

    def dequeue(self):
        if (self._stack1.empty()) and (self._stack2.empty()):
            raise ValueError()
        if self._stack2.empty():
            while not self._stack1.empty():
                self._stack2.push(self._stack1.pop())
        return self._stack2.pop()

    def max(self):
        if self._stack2.empty():
            return self._stack1.max()
        if self._stack1.empty():
            return self._stack2.max()
        return max(self._stack1.max(), self._stack2.max())


if __name__ == '__main__':
    n = int(input().strip())
    sequence = [int(x) for x in input().strip().split()]
    m = int(input().strip())
    queue = MaxQueue()
    maxs = [None for _ in range(n - m + 1)]
    if m > 0:
        for i in range(m):
            queue.enqueue(sequence[i])
        maxs[0] = queue.max()
        for i in range(m, n):
            queue.dequeue()
            queue.enqueue(sequence[i])
            maxs[i - m + 1] = queue.max()
    print(*maxs)
