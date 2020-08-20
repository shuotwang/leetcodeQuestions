import math

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def brute_force(P):
    min_d = float('inf')
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            min_d = min(min_d, dist(P[i], P[j]))
    return min_d


def closest_recursive(P):
    if len(P) <= 3:
        return brute_force(P)

    mid_idx = len(P) // 2
    mid_point = P[mid_idx]
    left = closest_recursive(P[:mid_idx])
    right = closest_recursive(P[mid_idx:])
    min_d = min(left, right)

    strip = []
    for p in P:
        if abs(p[0] - mid_point[0]) < min_d:
            strip.append(p)

    return min(min_d, closest_strip(strip, min_d))


def closest_strip(strip, d):

    min_d = d
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        j = i+1
        while j < len(strip) and abs(strip[i][1] - strip[j][1]) < min_d:
            min_d = dist(strip[i], strip[j])

    return min_d


def closest_pair(P):
    # pre-process: sort the points according to x axis
    P.sort(key=lambda point: point[0])

    return math.sqrt(closest_recursive(P))


points = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
print(closest_pair(points))