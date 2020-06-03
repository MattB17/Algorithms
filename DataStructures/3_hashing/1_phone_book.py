#python3
from random import randint


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


class Contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name

class ListItem():
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class HashChain():
    def __init__(self):
        self.head = None

    def push_front(self, number, name):
        key = Contact(number, name)
        item = ListItem(key)
        if self.head is None:
            self.head = item
        else:
            item.next = self.head
            self.head = item

    def find(self, number):
        curr_node = self.head
        while (curr_node is not None):
            if curr_node.key.number == number:
                return curr_node.key.name
            curr_node = curr_node.next
        return "not found"

    def delete(self, number):
        if self.head is None:
            return
        if self.head.key.number == number:
            self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next
            while (curr is not None):
                if curr.key.number == number:
                    prev.next = curr.next
                    break
                prev = curr
                curr = curr.next


class PhoneHash:
    def __init__(self, hash_size, prime_number):
        self.a = randint(1, prime_number - 1)
        self.b = randint(0, prime_number - 1)
        self.hash_size = hash_size
        self.prime = prime_number
        self.table = [HashChain() for _ in range(hash_size)]

    def get_hash(self, number):
        remainder = ((self.a * number) + self.b) % self.prime
        return remainder % self.hash_size

    def delete(self, number):
        hash_val = self.get_hash(number)
        self.table[hash_val].delete(number)

    def find(self, number):
        hash_val = self.get_hash(number)
        return self.table[hash_val].find(number)

    def add(self, number, name):
        hash_val = self.get_hash(number)
        self.table[hash_val].delete(number)
        self.table[hash_val].push_back(number, name)


def process_queries(queries, phone_hash):
    result = []
    for query in queries:
        if query.type == 'add':
            phone_hash.add(query.number, query.name)
        elif query.type == 'del':
            phone_hash.delete(query.number)
        else:
            result.append(phone_hash.find(query.number))
    return result


if __name__ == '__main__':
    n = int(input().strip())
    queries = [Query(input().strip().split()) for _ in range(n)]
    phone_hash = PhoneHash(1000, 10000019)
    query_results = process_queries(queries, phone_hash)
    print('\n'.join(query_results))
