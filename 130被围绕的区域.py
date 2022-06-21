from typing import List

# 是错误的解法
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def IsAround(i, j):
            if board[i][j] == "X":
                return True
            if board[i][j] == "O" and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                return False
            board[i][j] = "X"
            print(i,j,"设置为X")
            if IsAround(i - 1, j) and IsAround(i + 1, j) and IsAround(i, j - 1) and IsAround(i, j + 1):
                return True
            else:
                board[i][j] = "O"
                print(i, j, "将改回到O")
                return False

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O":
                    IsAround(i, j)
        print(board)


b = [["O", "X", "X", "O", "X"],
     ["X", "O", "O", "X", "O"],
     ["X", "O", "X", "O", "X"],
     ["O", "X", "O", "O", "O"],
     ["X", "X", "O", "X", "O"]]
Solution().solve(b)
