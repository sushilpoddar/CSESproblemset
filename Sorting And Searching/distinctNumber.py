"""this is a problem in which we have to find all distinct number from a list
"""
n = int(input())
val = list(map(int, input().split()))
print(len(set(val)))