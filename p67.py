#!/usr/bin/python

#import sys


#filename = sys.argv[1]
filename = "p067_triangle.txt"

file = open(filename)
pyramid = map(lambda x: map(lambda y: int(y), x.split(' ')), file.read().strip().split('\n'))
file.close()


cache = {}
def FindMaxSum(level, index):
	maxSum = cache.get((level, index))
	if (maxSum):
		return maxSum
	else:
		nextLevel = level + 1
		if nextLevel == len(pyramid):
			return pyramid[level][index]
		else:
			left = FindMaxSum(nextLevel, index)
			right = FindMaxSum(nextLevel, index + 1)
			maxSum = pyramid[level][index] + max(left, right)
			cache[(level, index)] = maxSum
			return maxSum

print FindMaxSum(0, 0)


