class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: 
        if not grid or grid[0][0]==1 or grid[-1][-1]==1:
            return -1             
        n = len(grid)
        q = deque([(0,0,1)])
        visit = set((0,0))
        directions = [[0,1], [0,-1], [-1,0], [1,0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while q:
            r, c, length = q.popleft()
            if r == n-1 and c == n-1:
                return length
            
            for dr, dc in directions:
                mr, mc = r + dr, c + dc
                if (0 <=mr <n and 0 <= mc <n
                    and (mr,mc) not in visit
                    and  grid[mr][mc] == 0):
                    q.append((mr,mc,length + 1))
                    visit.add((mr,mc))
        return -1

# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:       
#         if grid[0][0] == 1:
#             return -1
#         grid[0][0] = 1
#         queue = deque([(1, 0, 0)]) # path_length, row, column
#         directions = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
#         n = len(grid)
        
#         while queue:
#             path_length, row, column = queue.popleft()
#             if (row, column) == (n-1, n-1):
#                 return path_length
            
#             for dr, dc in directions:
#                 x = row + dr
#                 y = column + dc
#                 if (0 <= x < n and 0 <= y < n and not grid[x][y]):
#                     grid[x][y] = 1
#                     queue.append((1+path_length, x,y))
        
#         return -1

# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
#         if grid[0][0] != 0:
#             return -1

#         # Simple bfs we store, (r,c,length)
#         ROWS, COLS = len(grid), len(grid[0])
#         q = deque([(0,0,1)])
#         visited = set()
#         visited.add((0,0))

#         while q:
#             r, c, length = q.popleft()

#             if r == c == ROWS-1:
#                 return length

#             for dx, dy in [[0,1], [0,-1], [-1,0], [1,0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
#                 x = r + dx
#                 y = c + dy

#                 if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 0 and (x, y) not in visited:
#                     q.append((x, y, length+1))
#                     visited.add((x, y))

#         return -1

# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         if not grid or grid[0][0]==1 or grid[-1][-1]==1:
#             return -1        
#         n = len(grid)
#         visit = set()

#         def bfs(r,c):
#             q = collections.deque()
#             visit.add((r,c))
#             q.append((r,c))
#             length = 1

#             while q:
#                 size = len(q)  # Get the current size of the queue to track levels
#                 for _ in range(size):  # Iterate over the current level
#                     row, col = q.popleft()
#                     directions = [[0,1], [0,-1], [-1,0], [1,0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

#                     if row == n - 1 and col == n - 1:
#                         return length

#                     for dr, dc in directions:
#                         nr, nc = row + dr, col + dc
#                         if (nr in range(n) and
#                             nc in range(n) and
#                             grid[nr][nc] == 0 and (nr, nc) not in visit):
#                             q.append((nr, nc))
#                             visit.add((nr, nc))

#                 length += 1  # Increment the length for each level of traversal
                        
#             return -1


#         return bfs(0,0) 
        