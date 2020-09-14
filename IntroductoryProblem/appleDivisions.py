# """this is a problem of division of apple weight in two group so that
# difference between both group is minimum.
# """
#
#
# def findmin(i, s):
# 	global res, a
# 	if i == n:
# 		sumset1 = s
# 		sumset2 = t - s
# 		res = min(abs(sumset1-sumset2), res)
# 		return
# 	# exculude i element
# 	findmin(i+1, s)
#
# 	# include i element
# 	findmin(i+1, s+a[i])
#
#
# n = int(input())
# a = list(map(int, input().split()))
# t = sum(a)
# res = t
# findmin(0, 0)
# print(res)

