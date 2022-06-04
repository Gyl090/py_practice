from 剑指12矩阵中的路径 import Solution

solution = Solution()

board = [["C", "A", "A"],
         ["A", "A", "A"],
         ["B", "C", "D"]]
word = "AAB"

res = solution.exist(board, word)
print(res)
