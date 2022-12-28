def island(grid):
    valid = []
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            if (explore(grid,r,c,valid) == True):
                count+=1
    return count




def explore(grid,r,c,valid):
    rowInbound = ((0 <= r) & (r < len(grid)))
    colInbount = ((0<=c) & (c< len(grid)))

    if (not rowInbound or not colInbount):
        return False

    if (grid[r][c] == 'W'):
            return False

    pos = str(r)+','+str(c)

    if pos in valid:
        return False
    valid.append(pos)

    explore(grid, r - 1,c, valid)
    explore(grid, r + 1, c, valid)
    explore(grid, r, c-1, valid)
    explore(grid, r, c+1, valid)
    return True

w = [
    ['W','L','W','W','W'],
    ['W','L','W','W','W'],
    ['W','W','W','L','W'],
    ['W','W','L','L','W'],
    ['L','W','W','L','L'],

]



print(island(w))

