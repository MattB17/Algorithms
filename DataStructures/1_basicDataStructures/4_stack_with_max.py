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


if __name__ == '__main__':
    stack = StackWithMax()
    query_count = int(input().strip())
    queries = [None for _ in range(query_count)]
    for i in range(query_count):
        queries[i] = input().strip().split()
    for query in queries:
        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert False
