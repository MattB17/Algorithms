#python3
import math


class Processor():
    def __init__(self, process_num):
        self.process_num = process_num
        self.next_availability = 0

    def assign_task(self, task_duration):
        self.next_availability += task_duration

    def available_first(self, other_processor):
        return ((self.next_availability < other_processor.next_availability)
                or ((self.next_availability == other_processor.next_availability)
                and (self.process_num < other_processor.process_num)))


def left_child(i):
    return 2*i + 1


def right_child(i):
    return 2*i + 2


def parent(i):
    return math.floor((i - 1) / 2)


def sift_down_top(process_list, n):
    curr_idx = 0
    less_than_children = False
    while (not less_than_children) and (curr_idx < n):
        min_idx = curr_idx
        l = left_child(curr_idx)
        if l < n and process_list[l].available_first(process_list[min_idx]):
            min_idx = l
        r = right_child(curr_idx)
        if r < n and process_list[r].available_first(process_list[min_idx]):
            min_idx = r
        if curr_idx != min_idx:
            process_list[curr_idx], process_list[min_idx] = process_list[min_idx], process_list[curr_idx]
            curr_idx = min_idx
        else:
            less_than_children = True


def assign_jobs(process_list, jobs, n):
    for job in jobs:
        print(process_list[0].process_num, process_list[0].next_availability)
        process_list[0].assign_task(job)
        sift_down_top(process_list, n)


if __name__ == '__main__':
    processes, job_count = [int(x) for x in input().strip().split()]
    process_list = [Processor(i) for i in range(processes)]
    jobs = [int(x) for x in input().strip().split()]
    assign_jobs(process_list, jobs, processes)
