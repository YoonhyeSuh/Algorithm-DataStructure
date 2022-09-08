import sys
num = int(sys.stdin.readline())
xy = []

for i in range(num) :
    x,y = map(int, input().split())
    xy.append([y,x])

xy = sorted(xy)

for y,x in xy:
    print(x,y)