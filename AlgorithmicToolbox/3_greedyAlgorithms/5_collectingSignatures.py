#python3
import sys


def is_in_segment(x, segment):
    return segment[0] <= x <= segment[1]


def optimal_points(segments):
    points = []
    segments.sort(key=lambda segment: segment[1])
    while segments != []:
        endpoint = segments[0][1]
        segments = [segment for segment in segments
                    if not is_in_segment(endpoint, segment)]
        points.append(endpoint)
    return points



if __name__ == '__main__':
    n, *data = map(int, sys.stdin.read().split())
    segments = list(map(lambda x: (x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
