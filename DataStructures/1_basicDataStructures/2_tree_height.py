#python3



class Node():
    def __init__(self, key, next=None):
        self.key = key
        self.next = None


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


class QueueLL():
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def enqueue(self, key):
        node = Node(key)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def see_top(self):
        if self.head is None:
            raise ValueError()
        return self.head.key

    def dequeue(self):
        if self.head is None:
            raise ValueError()
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        return node.key

    def see_last(self):
        if self.tail is None:
            raise ValueError()
        return self.tail.key


def compute_height(n, parents):
    heights = [None for _ in range(n)]
    max_height = 0
    compute_queue = QueueLL()
    unresolveds = {}
    for i in range(n):
        if (parents[i] == -1) or (heights[parents[i]] is not None):
            compute_queue.enqueue(i)
            while not compute_queue.empty():
                idx = compute_queue.dequeue()
                if parents[idx] == -1:
                    height = 1
                else:
                    height = heights[parents[idx]] + 1
                heights[idx] = height
                if height >= max_height:
                    max_height = height
                if idx in unresolveds:
                    while not unresolveds[idx].empty():
                        compute_queue.enqueue(unresolveds[idx].pop())
                    del unresolveds[idx]
        else:
            if parents[i] not in unresolveds:
                unresolveds[parents[i]] = StackLL()
            unresolveds[parents[i]].push(i)
    return max_height


if __name__ == '__main__':
    n = int(input().strip())
    parents = [int(x) for x in input().strip().split()]
    print(compute_height(n, parents))
