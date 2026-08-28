class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #maxing a set for the iterable 
        rows = set()
        cols = set()
        #finding the row and col for iterating
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        #creating the row and col for iterating
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j]=0
        
        



