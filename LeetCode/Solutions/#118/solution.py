class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for row in range(1, numRows + 1):
            currRow = []
            for col in range(1, row + 1):
                if col == 1 or col == row:
                    currRow.append(1)
                else:
                    currRow.append(tri[row - 2][col - 2] + tri[row - 2][col - 1])
            tri.append(currRow)
        return tri
