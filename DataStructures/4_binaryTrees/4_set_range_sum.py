#python3
import sys


class Node:
    def __init__(self, key, sum, left, right, parent):
        self.key = key
        self.sum = sum
        self.left = left
        self.right = right
        self.parent = parent

    def left_sum(self):
        return self.left.sum if self.left is not None else 0

    def right_sum(self):
        return self.right.sum if self.right is not None else 0

    def update(self):
        self.sum = self.key + self.left_sum() + self.right_sum()
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self

    def small_rotation(self):
        parent = self.parent
        if parent is None:
            return
        grandparent = parent.parent
        if parent.left == self:
            m = self.right
            self.right = parent
            parent.left = m
        else:
            m = self.left
            self.left = parent
            parent.right = m
        parent.update()
        self.update()
        self.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = self
            else:
                grandparent.right = self

    def big_rotation(self):
        if self.parent.left == self and self.parent.parent.left == self.parent:
            self.parent.small_rotation()
            self.small_rotation()
        elif self.parent.right == self and self.parent.parent.right == self.parent:
            self.parent.small_rotation()
            self.small_rotation()
        else:
            self.small_rotation()
            self.small_rotation()

    def left_descendent(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr

    def right_ancestor(self):
        curr = self
        while curr is not None:
            if curr.parent is not None and curr.key < curr.parent.key:
                return curr.parent
            curr = curr.parent
        return None

    def splay(self):
        while self.parent is not None:
            if self.parent.parent is None:
                self.small_rotation()
                break
            self.big_rotation()


class SplayTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        curr = self.root
        last = self.root
        next = None
        while curr is not None:
            if curr.key >= key and (next is None or curr.key < next.key):
                next = curr
            last = curr
            if curr.key == key:
                break
            if curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        if last is not None:
            last.splay()
        self.root = last
        return next

    def next(self, key):
        node = self.find(key)
        if node.right is not None:
            return node.right.left_descendent()
        return node.right_ancestor()

def split(tree, key):
    result = tree.find(key)
    if result is None:
        return (tree, SplayTree())
    result.splay()
    right = SplayTree()
    right.root = result
    left = SplayTree()
    left.root = right.root.left
    right.root.left = None
    if left.root is not None:
        left.root.parent = None
        left.root.update()
    right.root.update()
    return (left, right)


def merge(left, right):
    if left.root is None:
        return right
    if right.root is None:
        return left
    curr = right.root
    while curr.left is not None:
        curr = curr.left
    curr.splay()
    right.root = curr
    right.root.left = left.root
    right.root.update()
    return right


class SplaySet:
    def __init__(self, m):
        self.m = m
        self.x = 0
        self.tree = SplayTree()

    def compute_val(self, key):
        return (key + self.x) % self.m

    def insert(self, key):
        val = self.compute_val(key)
        left, right = split(self.tree, val)
        new_node = None
        if right.root is None or right.root.key != val:
            new_node = Node(val, val, None, None, None)
        new_tree = SplayTree()
        new_tree.root = new_node
        self.tree = merge(merge(left, new_tree), right)
        self.tree.root.update()

    def erase(self, key):
        val = self.compute_val(key)
        node = self.tree.find(val)
        if node is None:
            return
        next = self.tree.next(val)
        if next is None:
            node.splay()
        else:
            next.splay()
            node.splay()
            next.update()
        if node.key != val:
            r = node
        elif next is None:
            r = node.left
        else:
            l = node.left
            r = node.right
            r.left = l
            if l is not None:
                l.parent = r
                l.update()
        if r is not None:
            r.update()
            r.parent = None
        self.tree.root = r

    def search(self, key):
        val = self.compute_val(key)
        node = self.tree.find(val)
        if node is None or node.key != val:
            return "Not found"
        return "Found"

    def sum(self, low, high):
        low = self.compute_val(low)
        high = self.compute_val(high)
        left, middle = split(self.tree, low)
        middle, right = split(middle, high + 1)
        self.x = 0 if middle.root is None else middle.root.sum
        self.tree = merge(merge(left, middle), right)
        return self.x


if __name__ == "__main__":
    splay_set = SplaySet(1000000001)
    n = int(input().strip())
    results = []
    for i in range(n):
        line = input().strip().split()
        if line[0] == '+':
            splay_set.insert(int(line[1]))
        elif line[0] == '-':
            splay_set.erase(int(line[1]))
        elif line[0] == '?':
            results.append(splay_set.search(int(line[1])))
        elif line[0] == 's':
            results.append(str(splay_set.sum(int(line[1]), int(line[2]))))
    print("\n".join(results))
