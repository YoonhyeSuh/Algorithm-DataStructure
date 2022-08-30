import sys, heapq
input = sys.stdin.readline
inf = 1e10

def dij(x):
    priority = []
    heapq.heappush(priority, (0, x))
    distance = [inf] * nodes; distance[0] = -1
    distance[x] = 0
    while priority:
        weight, N = heapq.heappop(priority)
        for new_weight, new_node in M[N]:
            if new_weight + weight < distance[new_node]:
                distance[new_node] = weight + new_weight
                heapq.heappush(priority, (weight + new_weight, new_node))
    return distance

tc = int(input())
for _ in ' '*tc:
    nodes, roads, destinations = map(int, input().split()); nodes += 1
    start, passing1, passing2 = map(int, input().split())
    
    M = list(list() for _ in ' '*nodes)
    for _ in ' '*roads:
        x, y, z = map(int, input().split())
        M[x].append([z, y])
        M[y].append([z, x])

    destinations = list(int(input()) for _ in ' '*destinations)
    shortest = [0] * nodes
    for i in (start, passing1, passing2):
        shortest[i] = dij(i)

    ans = []
    for i in destinations:
        tmp = min(shortest[start][passing1] + shortest[passing1][passing2] + shortest[passing2][i],\
                  shortest[start][passing2] + shortest[passing2][passing1] + shortest[passing1][i])
        if tmp <= shortest[start][i]:
            ans.append(i)

    for i in sorted(ans):
        print(i, end = " ")
    print()

