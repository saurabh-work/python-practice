from collections import deque
from typing import List
from collections import OrderedDict
import math

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def isValid(x, y):
            return x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0])

        visited = [[0] * len(maze[0]) for _ in range(len(maze))]
        min_d = math.inf
        q = [(start, 0)]

        while (q):
            node, dist = q.pop(0)
            visited[node[0]][node[1]] = 1
            x, y = node[0], node[1]
            nbrs = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
            for i, j in nbrs:
                if (not isValid(i, j)):
                    continue
                if (destination == [i, j]):
                    min_d = min(min_d, dist + 1)
                elif (visited[i][j] == 0 and maze[i][j] == 0):
                    q.append(([i, j], dist + 1))
        return min_d

sol = Solution()
test = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]

# [0,0,1,0,0],
# [0,0,0,0,0],
# [0,0,0,1,0],
# [1,1,0,1,1],
# [0,0,0,0,0]

import random

random.randint()

output = sol.shortestDistance(test, [0,4], [4,4])
print(output)