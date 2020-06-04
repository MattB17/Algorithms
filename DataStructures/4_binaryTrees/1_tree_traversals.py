#python3
import sys


class Node:
    def __init__(self, node):
        self.key = node[0]
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


def in_order(tree, n):
    traversal = [None for _ in range(n)]
    visit_count = 0
    current_node = tree[0]
    unvisited_stack = StackLL()
    unvisited_stack.push(current_node)
    while (visit_count < n):
        if current_node is None:
            current_node = unvisited_stack.pop()
            traversal[visit_count] = current_node.key
            visit_count += 1
            if current_node.right != -1:
                current_node = tree[current_node.right]
                unvisited_stack.push(current_node)
            else:
                current_node=None
        elif current_node.left != -1:
            current_node = tree[current_node.left]
            unvisited_stack.push(current_node)
        else:
            current_node = None
    return traversal


def pre_order(tree, n):
    traversal = [None for _ in range(n)]
    current_node = tree[0]
    traversal[0] = current_node.key
    visited_stack = StackLL()
    visited_stack.push(current_node)
    visit_count = 1
    while (visit_count < n):
        if current_node is None:
            current_node = visited_stack.pop()
            if current_node.right != -1:
                current_node = tree[current_node.right]
                traversal[visit_count] = current_node.key
                visit_count += 1
                visited_stack.push(current_node)
            else:
                current_node=None
        elif current_node.left != -1:
            current_node = tree[current_node.left]
            traversal[visit_count] = current_node.key
            visit_count += 1
            visited_stack.push(current_node)
        else:
            current_node = None
    return traversal


def post_order(tree, n):
    traversal = [None for _ in range(n)]
    visit_count = 0
    tree[0].seen = True
    current_node = tree[0]
    unvisited_stack = StackLL()
    unvisited_stack.push(current_node)
    while (visit_count < n):
        if current_node is None:
            right_child = unvisited_stack.front().right
            if ((right_child == -1) or (tree[right_child].seen)):
                traversal[visit_count] = unvisited_stack.pop().key
                visit_count += 1
                current_node = None
            else:
                tree[right_child].seen = True
                current_node = tree[right_child]
                unvisited_stack.push(current_node)
        elif current_node.left != -1:
            tree[current_node.left].seen = True
            current_node = tree[current_node.left]
            unvisited_stack.push(current_node)
        else:
            current_node = None
    return traversal


if __name__ == '__main__':
    n = int(input().strip())
    tree = [None for _ in range(n)]
    for i in range(n):
        tree[i] = Node(input().strip().split())
    print(" ".join(in_order(tree, n)))
    print(" ".join(pre_order(tree, n)))
    print(" ".join(post_order(tree, n)))
