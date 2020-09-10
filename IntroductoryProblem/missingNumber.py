n = int(input())
# print(n*(n+1)//2-sum([int(i) for i in input().split()]))
print(sum(range(1, n+1))-sum([int(i) for i in input().split()]))
