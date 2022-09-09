import sys
input = sys.stdin.readline
MAX_COOR = 100000

"""
3089번 네잎 클로버를 찾아서
상당히 까다로운 문제입니다.
문제를 요약하면,
'좌표를 줄게, 그리고 방향을 순서대로 몇 개 줄테니 해당 방향으로 그 좌표중 가장 가까운 곳까지 가자.
그러면 마지막 명령을 실행한 후에 넌 어떤좌표에 있을까?'
이 때, 주는 방향으로 가다보면 주었던 좌표가 적어도 하나 있다는 보장이 있습니다.
이제 문제를 푸는 방법을 생각해봅시다.

일단 자기가 서있는 좌표로부터 가장 가까운 방향을 골라내야겠죠.
예를들어 좌표가 (0,1), (0,2), (0,-1)이 있고, 위로 올라가라는 명령을 받았다 합시다. 초기좌표는 (0,0)이고요.
그러면 일단 (0,-1)은 아래로 가는 방향이니 제외하고, (0,1), (0,2)중 더 가까운 좌표로 가야할겁니다.
결국, U명령을 한번 받으면 (0,1)로 이동할겁니다.
'입력받은 좌표 중 내 좌표에서 한 방향으로 갈 때 가장 가까운 좌표를 추적해야한다'
'상하좌우 한 방향으로만 움직이므로 2차원 좌표계에서 신경쓸 필요가 없다.'
이 말은 곧 이분탐색을 하면 좀 편할거라는 뜻이겠죠.

좌표 한 번 찾는데, 즉 명령 한번 수행에 O(lgN), 명령 총 M(<=100000)번 수행에 O(MlgN).
X와 Y좌표에서 각각 정렬을 해야하니 대충 O(NlgN)이 두 번. 이차원이라 좀 더 들지만 그건 감안합시다.
결국, O((N+M)lgN)으로 모든 명령을 처리할 수 있는거로 보입니다.
시간복잡도 계산은 잘 안해봤어서 좀 헷갈리긴한데..
"""

"""
먼저 이분탐색을 만들어봅시다.
코틀린에선 binarysearch로, C++에선 lowerbound로 바로 사용 가능하지만.
이 문제는 그냥 그거 쓰긴 힘들어보입니다. 어차피 파이썬은 없기도 하니, 직접 만들어봅시다.

upperbound는 정렬된 배열에서 찾는 숫자보다 크고, 찾는 숫자와 가장 가까운 수의 인덱스를 반환합니다.
lowerbound는 정렬된 배열에서 찾는 숫자이거나 그보다 크고, 그 숫자와 가장 가까운 수의 인덱스를 반환합니다.
즉, [1,2,3,4,5]에서 upperbound(3)을 쓰면 3을, lowerbound(3)을 쓰면 2를 반환합니다. 인덱스인것에 유의합시다.

upperbound로 하면 더 작은 좌표를 찾아내는데에 약간의 불편함이 발생하니 저는 lowerbound로 할거고요.
l, r은 lowerbound를 사용해보셨다면 어떤건지 아실겁니다. 탐색하는 범위입니다.
흔히, C++ 벡터의 lowerbound에선 vector.bigin(), vector.end()이었나. 그 부분입니다.
원래라면 l = 0, r = len(arr)-1 고정이지만 이 문제에선 이분탐색을 두 번 써야합니다.
그러니, 인자로 받아옵시다.

find는 찾는 숫자입니다. arr은 array, 즉 배열이구요. XorY는 X와 Y중 뭘 탐색할건지 확인하는겁니다.
0은 X, 1은 Y입니다.
"""
def lowerbound(l, r, find, arr, XorY): # 0 is X, 1 is Y
    r -= 1
    while l < r:
        m = l + r >> 1
        if arr[m][XorY] >= find:
            r = m
        else:
            l = m+1
    return r

"""
lowerbound를 두 번 사용해야합니다. fix는 아시다시피 '고정하다'란 뜻으로, 좌우를 가면 Y가 고정되고, 위아래를 가면 X가 고정됨을 이용했습니다.
첫 lowerbound는 필요한 배열의 전체를 탐색합니다. 다시말해 현재 x 혹은 y좌표와 같은게 시작되는 인덱스를 찾아냅니다.
xcoor_cnt와 ycoor_cnt는 밑에 나오는데, 각 x, y좌표가 몇 개씩 있는지 체크를 해둔 배열입니다.
예를들어서, (1,0), (2,0), (1,1)을 입력받았다면 ycoor_cnt[1+100000]에 1이, xcoor_cnt[1+100000]에는 2가, xcoor_cnt[2+100000]에는 1이 들어갑니다.
100000을 더해주는 이유는 최솟값이 -100000이라, 배열에 저장할 수 없어 일괄적으로 100000을 더해 저장했습니다.
시작부분에 MAX_COOR가 100000이 되어 있는이유는, -100000<=x,y<=100000이기 때문입니다.

어쨌든, 다음 lowerbound는
l이 '고정된 x 혹은 y좌표가 시작하는 좌표'
r이 '현재 x 혹은 y 좌표의 끝'
(현재 y가 y배열에서 3인덱스부터 시작하고, 현재 y가 y배열에 3개 있다면, 3~5 인덱스에 현재 y좌표가 있겠죠.
다른건 x좌표 뿐일테니, 그걸 이용해서 찾아주는겁니다. 모르겠으면 밑에 main함수에서 해당 배열이 어떻게 수가 정해지는지 보고옵시다.)
find_x는 오른쪽이나 위쪽으로 가면 1을 더해주고 (lowerbound 특징 이용)
arr에는 고정된 y나 x 배열을 써줍니다.
0, 1은 위에 있다시피 XorY부분입니다.
"""
def fix_y_lowerbound(now_y, find_x, isR = 0):
    nyi = lowerbound(0, clover, now_y,  y, 1) #now_y_idx
    return lowerbound(nyi, nyi+ycoor_cnt[now_y+MAX_COOR], find_x+isR, y, 0)

def fix_x_lowerbound(now_x, find_y, isU = 0):
    nxi = lowerbound(0, clover, now_x, x, 0) #now_x_idx
    return lowerbound(nxi, nxi+xcoor_cnt[now_x+MAX_COOR], find_y+isU, x, 1)

"""
메인함수입니다.
먼저 클로버의 개수, 명령어의 개수를 입력받아주고,
coordinate에서 따온 coor에 좌표를 받아적어줍시다.
"""
clover, command = map(int, input().split())
coor = []

"""
x, y좌표에 몇 개의 해당 좌표가 있는지 파악하는건 중요합니다.
-좌표계까지 감안해서, 양수 배열의 두 배 크기로 만들어줍시다.
coor에 하나씩 좌표를 넣어주고, xcoor_cnt에 방금 들어간 x좌표에 1개가 더 들어왔다 표시해주고, ycoor_cnt도 같이 해줍니다.
[0]은 x를, [1]은 y를 나타냅니다.
"""
xcoor_cnt = [0]*(2*MAX_COOR+1)
ycoor_cnt = [0]*(2*MAX_COOR+1)
for _ in ' '*clover:
    coor.append(list(map(int, input().split())))
    xcoor_cnt[coor[-1][0]+MAX_COOR] += 1
    ycoor_cnt[coor[-1][1]+MAX_COOR] += 1
"""
C면 이차원 배열 정렬까지 직접 해야하는 기적을 일으켜야했겠으나,
다행히 여기서는 제공해줍니다.
"""
x = sorted(coor) # x기준 정렬
y = sorted(coor, key = lambda x: (x[1], x[0])) # y기준 정렬

"""
거의 다 했습니다. C에 명령어를 입력받고, 현재 좌표를 now_coor에 지정합시다.
현 좌표가 0 0인건 문제에서 준 정보입니다.
명령언 LRUD로 주어집니다. 뭔뜻인진 대충 보시면 아실거라 생각합니다.
RU에는 isR, isU에 1을 넣어줍니다. 위에서 말했듯이 lowerbound의 특성을 이용한겁니다.
[1,2,3,7,9]처럼 중복된 원소가 없는 정렬된 배열에서 3보다 큰 수를 찾고싶다면 3+1의 lowerbound값을 찾으면 되겠죠.
4보다 큰 첫 인덱스는 3이니, 3을 출력할겁니다.
이걸 이용한겁니다.
"""
C = list(input().rstrip())
now_coor = [0, 0]
for c in C:
    if c == 'L':
        now_coor = y[fix_y_lowerbound(now_coor[1], now_coor[0], 0)-1]
    elif c == 'R':
        now_coor = y[fix_y_lowerbound(now_coor[1], now_coor[0], 1)]
    elif c == 'U':
        now_coor = x[fix_x_lowerbound(now_coor[0], now_coor[1], 1)]
    elif c == 'D':
         now_coor = x[fix_x_lowerbound(now_coor[0], now_coor[1], 0)-1]
print(*now_coor)
