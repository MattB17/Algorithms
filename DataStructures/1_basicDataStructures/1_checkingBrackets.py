#python3


class Node():
    def __init__(self, char, position, next=None):
        self.char = char
        self.position = position
        self.next = next


class StackLL():
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, char, position):
        node = Node(char, position)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def pop(self):
        if self.empty():
            raise ValueError()
        node = self.head
        self.head = node.next
        return node


def find_mismatch(text):
    bracket_stack = StackLL()
    for pos in range(len(text)):
        if text[pos] in "([{":
            bracket_stack.push(text[pos], pos)
        elif text[pos] in ")]}":
            if bracket_stack.empty():
                return pos + 1
            char = bracket_stack.pop().char
            if ((char == '(' and text[pos] != ')') or
                (char == '[' and text[pos] != ']') or
                (char == '{' and text[pos] != '}')):
                return pos + 1
    if bracket_stack.empty():
        return -1
    return bracket_stack.pop().position + 1


if __name__ == "__main__":
    text = input().strip()
    mismatch = find_mismatch(text)
    print("Success" if mismatch == -1 else mismatch)
