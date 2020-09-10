from itertools import permutations
string = sorted(input())
result = []
for i in sorted(set(permutations(string))):
	result.append("".join(i))
print(len(result))
print(*result, sep='\n')
