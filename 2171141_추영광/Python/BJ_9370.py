import sys, heapq
input = sys.stdin.readline # 파이썬으로 푸실 때 이거 잊으면 안됩니다!
inf = 1e10

"""
백준 9370번 미확인 도착지

단계별 '최단거리'에 있는 문제입니다.
문제 해결 방법을 쓸거니, 해결을 하신 후 읽으시는걸 추천드립니다.
문제의 난이도는 골드 2이지만, 골드 4 '특정한 최단경로'를 풀었다면 바로 푸실 수 있습니다.
다익스트라 알고리즘 최저난이도가 골드 4이니, 그냥 다익스트라 아시면 푸실 수 있는 문제입니다.


문제가 생각보단 짧지만 주는 정보가 매우 많습니다.
그 정보를 하나씩 설명하면서 가보겠습니다.
제한시간이 3초로 매우 깁니다. 하지만 쫄지 말고 그냥 풀어도 됩니다.
파이썬으로 해도 0.5초만에 실행이 끝납니다.


문제를 천천히 읽다보면 모든 간선의 가중치가 0 이상입니다.
아무래도 다익스트라 일고리즘 쓰는게 좋을것같습니다.
저는 다익스트라 배운지 20일만에 처음써보는거라 옛날에 푼 문제의 코드를 배끼다시피 썼는데요,
이 문제를 풀 때 먼저 풀어보면 좋은 문제는 1504번 특정한 최단 경로 입니다.
잘 비교해보면 두 문제는 같은 문제라는걸 알 수 있습니다.
"""
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

tc = int(input()) # tc는 test case를 뜻합니다.
for _ in ' '*tc:
    """
    문제에서 첫번째로 정수 n, m, t, 그리고 두번째 줄로 s, g, h를 준다고 합니다.
    쭉 뜯어보면, n은 '노드의 개수', m은 '간선의 개수', t는 '목적지 노드의 개수'
    s는 '출발노드', g와 h는 '반드시 지나야 하는 노드'로 해석 할 수 있습니다.

    g와 h는 왜 주어졌는지 한 3분정도 고민했습니다. 문제 열 번정도 다시 읽으니 이해가 갔었습니다.
    노드의 개수와 같은 경우에는, 그래프는 문제에서 0을 언급하지 않는 이상 0번은 사용하지 않으니,
    1-Based로 사용하기 위해 nodes에 1을 더해둡니다.
    """
    nodes, roads, destinations = map(int, input().split()); nodes += 1
    start, passing1, passing2 = map(int, input().split())

    """
    저는 그래프 문제를 풀 때 받는 2차원 지도는 M으로 받습니다. Map에서 따왔습니다.
    여담으로, 수열과 같은 것을 받을 때는 arr로 받습니다.

    어쨌든, 이 도로들은 무방향 도로라고 합니다.
    그래프를 받아서 적어줍니다.
    """
    M = list(list() for _ in ' '*nodes)
    for _ in ' '*roads:
        x, y, z = map(int, input().split())
        M[x].append([z, y])
        M[y].append([z, x])

    """
    목적지의 개수를 위에서 받았었죠.
    목적지 노드가 어딘지 받아적어줍니다.

    shortest 변수는 다익스트라를 적용받을 변수입니다.
    다익스트라는 start, passing1, passing2에서만 받으면 되기에 그냥 해당 변수에 덮어씌워도 되지만,
    이렇게 쓰면 "shortest[출발점][도착점]" 으로 깔끔하게 쓸 수 있습니다.
    오늘 처음써봤는데 나름 괜찮은 방법 같습니다.
    """
    destinations = list(int(input()) for _ in ' '*destinations)
    shortest = [0] * nodes
    for i in (start, passing1, passing2):
        shortest[i] = dij(i)

    """
    이제 정답을 받아야겠죠.
    ans는 당연히 answer에서 따왔습니다.
    바로 위 문단에서 destinations변수로 목적지들을 담았습니다.
    
    이번 단계에서 할 일은,
    [출발점 - 첫 패싱 노드 - 두번째 패싱 노드 - 도착점], [출발점 - 두번째 패싱 노드 - 첫 패싱 노드 - 도착점]중
    더 작은 값을 tmp에 저장합니다.

    문제에서 '불가능한 목적지'를 적으라고 했습니다.
    이 뜻에 대해 3분정도 또 고민했는데, 결국 "[출발점 - 도착점] 이렇게 가는게 최단거리인 경우"를 제외하라. 라는 뜻입니다.
    문제에 보면 두 번째 테스트 케이스에 대하여 그림이 있습니다. 이 그림을 참고해보면
    가능한 목적지는 5, 6으로 두 개고 출발점은 2 이지만 [2 - 1 - 3 - 5]보다 [2 - 5]가 더 거리가 짧습니다.
    조건상, 이들은 최단거리로만 이동을 하고 돌아가지 않는다고 했으므로 5번은 결국 목적지가 될 수 없습니다.

    이 뜻은, shortest[start][i]의 값이 더 작은경우 목적지가 될 수 없다는 뜻입니다.
    if문을 이용해서 걸러주먼 끝날겁니다.
    """
    ans = []
    for i in destinations:
        tmp = min(shortest[start][passing1] + shortest[passing1][passing2] + shortest[passing2][i],\
                  shortest[start][passing2] + shortest[passing2][passing1] + shortest[passing1][i])
        if tmp <= shortest[start][i]:
            ans.append(i)

    """
    테스트케이스의 마지막, 출력부분입니다.
    print(*ans, sep='\n')의 경우 더 느리니,
    for문을 써서 출력을 하도록 합시다.
    대신, 마지막에 개행 하는 것도 잊지 말아야 합니다.
    """
    for i in sorted(ans):
        print(i, end = " ")
    print()
