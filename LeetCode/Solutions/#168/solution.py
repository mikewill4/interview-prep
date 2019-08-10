class Solution:
	def convertToTitle(self, n: int) -> str:
		output_str = ""
		while n > 26:
			char_n = chr(n % 26 + 64)
			output_str = char_n + output_str
			n = n // 26
		char_n = chr(n + 64)
		output_str = char_n + output_str
		return output_str
