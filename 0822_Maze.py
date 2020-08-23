class Solution:

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        row = len(maze)
        col = len(maze[0])

        def dfs(maze: List[List[int]], start: List[int], des: List[int], visited: set) -> bool:
            if (start[0], start[1]) in visited:
                return False

            if (start == des):
                return True

            visited.add((start[0], start[1]))

            l = start[1] - 1
            r = start[1] + 1
            u = start[0] - 1
            d = start[0] + 1

            while l >= 0 and maze[start[0]][l] == 0:
                l -= 1
            if dfs(maze, [start[0], l + 1], des, visited):
                return True

            while r < col and maze[start[0]][r] == 0:
                r += 1
            if dfs(maze, [start[0], r - 1], des, visited):
                return True

            while u >= 0 and maze[u][start[1]] == 0:
                u -= 1
            if dfs(maze, [u + 1, start[1]], des, visited):
                return True

            while d < row and maze[d][start[1]] == 0:
                d += 1
            if dfs(maze, [d - 1, start[1]], des, visited):
                return True

        return dfs(maze, start, destination, set())