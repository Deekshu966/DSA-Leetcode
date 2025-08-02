import numpy as np
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        np_matrix = np.array(matrix)

        # Step 1: Transpose the matrix
        transposed = np.transpose(np_matrix)

        # Step 2: Reverse each row using slicing
        rotated = transposed[:, ::-1]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = rotated[i][j]
        """
        
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
            