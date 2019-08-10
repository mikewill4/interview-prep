class Solution:
	def trailingZeroes(self, n: int) -> int:
		numZeroes = count = 0
		while count <= n:
			if count < 5:
				numZeroes = 0
			if count % 5 == 0:
				numZeroes += 1
			if count % 25 == 0:
				numZeroes += 1
			count += 1
		return numZeroes
