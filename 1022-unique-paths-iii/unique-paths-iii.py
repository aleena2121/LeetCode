class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        start,end = () ,()
        path = 2
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == 0:
                    path += 1

        visited= set()
        def dfs(start,end,curpath):
            if start in visited or grid[start[0]][start[1]] == -1:
                return 0
            if start == end:
                if curpath == path:
                    return 1
                else:
                    return 0
            
            count = 0
            visited.add(start)
            for x,y in [(0,1), (0,-1), (-1,0), (1,0)]:
                if 0<=(x + start[0])<ROW and 0<=(y + start[1])<COL:
                    count += dfs((x + start[0],y + start[1]), end,curpath+1)  
            visited.remove(start)
            return count
        
        return dfs(start,end,1)