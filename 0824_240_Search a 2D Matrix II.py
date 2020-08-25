class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        def helper(top, down, left, right):
            if top > down or left > right:
                return False

            if target < matrix[top][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2
            up = top
            while up <= down:
                if matrix[up][mid] == target:
                    return True
                up += 1
            return helper(top, down, left, mid - 1) or helper(top, down, mid + 1, right)

        return helper(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

