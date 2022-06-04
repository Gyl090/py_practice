from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        # dfs 表示对 (i,j) 位置开始搜索 k是要搜索的字符index
        def dfs(k: int, i: int, j: int) -> bool:
            # 越界 或 board[i][j]与需要的字符不符
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            # 要搜索的 的word的最后一个字母 且 (i,j)位置的字母就是 需要的字母
            if k == len(word) - 1 and board[i][j] == word[-1]:
                return True
            else:
                temp = board[i][j]
                board[i][j] = '#'
                ans = dfs(k + 1, i - 1, j) or dfs(k + 1, i + 1, j) or dfs(k + 1, i, j - 1) or dfs(k + 1, i, j + 1)
                board[i][j] = temp
                return ans

        for i in range(m):
            for j in range(n):
                res = dfs(0, i, j)
                if res:
                    return True
        return False