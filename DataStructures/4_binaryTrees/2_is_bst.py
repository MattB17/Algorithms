#python3
import sys


class Node:
    def __init__(self, node):
        self.key = int(node[0])
        self.left = int(node[1])
        self.right = int(node[2])
        self.seen = False


class StackItem:
    def __init__(self, node, next=None):
        self.node = node
        self.next = None


class StackLL():
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, node):
        item = StackItem(node)
        if self.head is not None:
            item.next = self.head
        self.head = item

    def pop(self):
        if self.empty():
            raise ValueError()
        item = self.head
        self.head = item.next
        return item.node

    def front(self):
        if self.empty():
            raise ValueError()
        return self.head.node


class StackWithMax():
    def __init__(self):
        self._values_stack = StackLL()
        self._max_stack = StackLL()

    def empty(self):
        return self._values_stack.empty()

    def push(self, node):
        self._values_stack.push(node)
        if ((self._max_stack.empty()) or
            (node.key >= self._max_stack.front().key)):
            self._max_stack.push(node)

    def pop(self):
        node = self._values_stack.pop()
        if node.key == self._max_stack.front().key:
            self._max_stack.pop()
        return node

    def max(self):
        return self._max_stack.front().key


class StackWithMin():
    def __init__(self):
        self._values_stack = StackLL()
        self._min_stack = StackLL()

    def empty(self):
        return self._values_stack.empty()

    def push(self, node):
        self._values_stack.push(node)
        if ((self._min_stack.empty()) or
            (node.key <= self._min_stack.front().key)):
            self._min_stack.push(node)

    def pop(self):
        node = self._values_stack.pop()
        if node.key == self._min_stack.front().key:
            self._min_stack.pop()
        return node

    def min(self):
        return self._min_stack.front().key


def is_bst(tree, n):
    if n == 0:
        return "CORRECT"
    left_parents = StackWithMin()
    right_parents = StackWithMax()
    directions = StackLL()
    tree[0].seen = True
    current_node = tree[0]
    visit_count = 0
    while (visit_count < n):
        if current_node is None:
            direction = directions.pop()
            if direction == "left":
                current_node = left_parents.pop()
                right_parents.push(current_node)
                directions.push("right")
                if ((current_node.right == -1) or
                    (tree[current_node.right].seen)):
                    current_node = None
                else:
                    current_node = tree[current_node.right]
            else:
                right_parents.pop()
                visit_count += 1
        elif ((not left_parents.empty()) and
              (left_parents.min() < current_node.key)):
              return "INCORRECT"
        elif ((not right_parents.empty()) and
              (right_parents.max() > current_node.key)):
              return "INCORRECT"
        else:
            left_parents.push(current_node)
            directions.push("left")
            if current_node.left == -1:
                current_node = None
            else:
                tree[current_node.left].seen = True
                current_node = tree[current_node.left]
    return "CORRECT"


if __name__ == "__main__":
    n = int(input().strip())
    tree = [None for _ in range(n)]
    for i in range(n):
        tree[i] = Node(input().strip().split())
    print(is_bst(tree, n))
