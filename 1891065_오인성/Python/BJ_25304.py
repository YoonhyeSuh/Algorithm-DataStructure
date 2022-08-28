import sys
costs = int(sys.stdin.readline())
num = int(sys.stdin.readline())

sum = 0

for i in range(num) : 
    cost,number = map(int, input().split())
    sum += (cost * number)

if(costs == sum) : print("Yes")
else : print("No")