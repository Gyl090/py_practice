from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        n, m = len(matrix), len(matrix[0])
        visited = set()
        ret = []
        turns = ['R', 'D', 'L', 'U']
        turn = turns[0]

        while len(visited) < m * n:
            # put (i,j) into ret, if it's time to turn, just do it
            # print(ret, visited)
            ret.append(matrix[i][j])
            visited.add((i, j))
            if turn == 'R':
                j += 1
                if j == m or (i, j) in visited:
                    turn = turns[1]
                    j -= 1
                    i += 1
                continue
            if turn == 'D':
                i += 1
                if i == n or (i, j) in visited:
                    turn = turns[2]
                    i -= 1
                    j -= 1
                continue
            if turn == 'L':
                j -= 1
                if j < 0 or (i, j) in visited:
                    turn = turns[3]
                    j += 1
                    i -= 1
                continue
            if turn == 'U':
                i -= 1
                if i < 0 or (i, j) in visited:
                    turn = turns[0]
                    i += 1
                    j += 1
                continue
        return ret


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
res = Solution().spiralOrder(matrix)
print(res)
