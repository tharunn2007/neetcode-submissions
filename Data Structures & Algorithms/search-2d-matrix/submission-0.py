class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h1 = len(matrix)-1
        l1 = 0

        while l1<=h1:
            m1 = (l1+h1)//2
            if target<matrix[m1][0]:
                h1 = m1-1
            elif target>matrix[m1][-1]:
                l1=m1+1
            elif matrix[m1][0]<=target<=matrix[m1][-1]:
                l2 = 0
                h2 = len(matrix[m1])-1
                while l2<=h2:
                    m2 = (l2+h2)//2
                    if target == matrix[m1][m2]:
                        return True
                    elif target>matrix[m1][m2]:
                        l2=m2+1
                    else:
                        h2=m2-1
                return False
        return False   