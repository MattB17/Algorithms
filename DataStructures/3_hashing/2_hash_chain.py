#python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class ListItem():
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class HashChain():
    def __init__(self):
        self.head = None

    def push_front(self, s):
        item = ListItem(s)
        if self.head is None:
            self.head = item
        else:
            item.next = self.head
            self.head = item

    def find(self, s):
        curr_node = self.head
        while (curr_node is not None):
            if curr_node.key == s:
                return "yes"
            curr_node = curr_node.next
        return "no"

    def delete(self, s):
        if self.head is None:
            return
        if self.head.key == s:
            self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next
            while (curr is not None):
                if curr.key == s:
                    prev.next = curr.next
                    break
                prev = curr
                curr = curr.next

    def __str__(self):
        nodes = []
        curr_node = self.head
        while (curr_node is not None):
            nodes.append(curr_node.key)
            curr_node = curr_node.next
        return " ".join(nodes)



class StringHash:
    def __init__(self, m, x, p):
        self.m = m
        self.x = x
        self.p = p
        self.table = [HashChain() for _ in range(m)]

    def get_hash(self, s):
        hash = 0
        for i in range(len(s)-1, -1, -1):
            hash = ((hash * self.x) + ord(s[i])) % self.p
        return hash % m

    def delete(self, s):
        hash_val = self.get_hash(s)
        self.table[hash_val].delete(s)

    def find(self, s):
        hash_val = self.get_hash(s)
        return self.table[hash_val].find(s)

    def add(self, s):
        hash_val = self.get_hash(s)
        if self.table[hash_val].find(s) == "no":
            self.table[hash_val].push_front(s)

    def check(self, idx):
        return str(self.table[idx])

def process_queries(queries, string_hash):
    result = []
    for query in queries:
        if query.type == "add":
            string_hash.add(query.s)
        elif query.type == "del":
            string_hash.delete(query.s)
        elif query.type == "find":
            result.append(string_hash.find(query.s))
        else:
            result.append(string_hash.check(query.ind))
    return result


if __name__ == "__main__":
    m = int(input().strip())
    q = int(input().strip())
    queries = [Query(input().strip().split()) for _ in range(q)]
    string_hash = StringHash(m, 263, 1000000007)
    query_results = process_queries(queries, string_hash)
    print("\n".join(query_results))
