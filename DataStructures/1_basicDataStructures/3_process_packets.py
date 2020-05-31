#python3


class Packet():
    def __init__(self, arrival_time, length, end_time=None):
        self.arrival_time = arrival_time
        self.length = length
        self.end_time = end_time


class Node():
    def __init__(self, key, next=None):
        self.key = key
        self.next = None


class QueueLL():
    def __init__(self):
        self.head = None
        self.tail = None

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


class Buffer():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = QueueLL()
        self.buffer_size = 0

    def remove_processed_by_timepoint(self, timepoint):
        while ((self.buffer_size > 0) and
                (self.queue.see_top().end_time <= timepoint)):
            self.queue.dequeue()
            self.buffer_size -= 1

    def process_packet(self, packet):
        self.remove_processed_by_timepoint(packet.arrival_time)
        if self.buffer_size == self.capacity:
            return -1
        if self.buffer_size == 0:
            start_time = packet.arrival_time
        else:
            start_time = self.queue.see_last().end_time
        packet.end_time = start_time + packet.length
        self.queue.enqueue(packet)
        self.buffer_size += 1
        return start_time

if __name__ == "__main__":
    capacity, packet_count = [int(x) for x in input().strip().split()]
    buffer = Buffer(capacity)
    start_times = [None for _ in range(packet_count)]
    for i in range(packet_count):
        arrival, length = [int(x) for x in input().strip().split()]
        packet = Packet(arrival, length)
        start_times[i] = buffer.process_packet(packet)
    for time in start_times:
        print(time)
