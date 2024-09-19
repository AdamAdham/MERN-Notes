import numpy as np
# Added feature
# direct push
def max_profit(grid):
    grid = np.array(grid)
    profit = np.zeros(grid.shape)
    path = np.zeros(grid.shape)
    x = 1 + 2
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(i==0 and j==0):
                profit[i][j] = grid[i][j]
                path[i][j] = [(i,j)]
            elif(i==0):
                profit[i][j] = grid[i][j-1] +  grid[i][j]
                path[i][j] = path[i][j-1] + [(i,j-1)]
            elif(j==0):
                profit[i][j] = grid[i-1][j] +  grid[i][j]
                path[i][j] = path[i-1][j] + [(i-1,j)]
            else:
                val,cord = get_max(grid[i-1][j],(i-1,j),grid[i][j-1],(i,j-1))
                profit[i][j] = val + grid[i][j]
                path[i][j] = path[i-1][j] + [cord]
    return x


def get_max(a,a_cord,b,b_cord):
    if(a>b):
        return a,a_cord
    else:
        return b,b_cord
