"""this is a problem of apartment in which we have some aprtment size
and have some people required apartment size and you have to
distribute apartment to people. apartment should be size of between
 (required-x) to (required+x)"""
n, m, k = map(int, input().split())
req = sorted(list(map(int, input().split())))
apar = sorted(list(map(int, input().split())))
ans = 0
i, j = 0, 0
while i < n and j < m:
    if abs(req[i] - apar[j]) <= k:
        ans += 1
        i += 1
        j += 1
    elif req[i] < apar[j]:
        i += 1
    else:
        j += 1
print(ans)
