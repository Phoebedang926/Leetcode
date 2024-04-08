class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        direct = [[0,1], [0,-1], [1,0], [-1,0]]
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh>0:     
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in direct:
                    nr, nc = row+dr, col+dc
                    if (0 <= nr < rows  and 0 <= nc < cols and
                        grid[nr][nc] == 1 ):
                        grid[nr][nc] = 2
                        q.append((nr,nc))    
                        fresh -=1
            time += 1

        return time if fresh == 0 else -1

        
        