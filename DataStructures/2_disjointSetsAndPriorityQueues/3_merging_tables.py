#python3


class Table:
    def __init__(self, row_count, idx):
        self.row_count = row_count
        self.parent = idx
        self.rank = 0


class Database:
    def __init__(self, tables):
        self.tables = tables
        self.max_row_count = max([table.row_count for table in tables])

    def find_parent(self, table_num):
        if table_num != self.tables[table_num].parent:
            self.tables[table_num].parent = self.find_parent(
                self.tables[table_num].parent)
        return self.tables[table_num].parent

    def merge(self, src, dst):
        src_parent = self.find_parent(src)
        dst_parent = self.find_parent(dst)
        if src_parent == dst_parent:
            return
        if self.tables[src_parent].rank > self.tables[dst_parent].rank:
            self.tables[dst_parent].parent = src_parent
            self.tables[src_parent].row_count += self.tables[dst_parent].row_count
            self.tables[dst_parent].row_count = 0
            self.max_row_count = max(
                self.max_row_count, self.tables[src_parent].row_count)
        else:
            self.tables[src_parent].parent = dst_parent
            self.tables[dst_parent].row_count += self.tables[src_parent].row_count
            self.tables[src_parent].row_count = 0
            self.max_row_count = max(
                self.max_row_count, self.tables[dst_parent].row_count)
            if self.tables[src_parent].rank == self.tables[dst_parent].rank:
                self.tables[dst_parent].rank += 1


if __name__ =='__main__':
    n_tables, n_queries = [int(x) for x in input().strip().split()]
    counts = [int(x) for x in input().strip().split()]
    tables = [Table(counts[i], i) for i in range(len(counts))]
    db = Database(tables)
    queries = [None for _ in range(n_queries)]
    for i in range(n_queries):
        dst, src = [int(x) for x in input().strip().split()]
        queries[i] = (dst, src)
    for dst, src in queries:
        db.merge(src - 1, dst - 1)
        print(db.max_row_count)
