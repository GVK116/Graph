import sys


def minimum(grid):
    visited,count = [],sys.maxsize
    for r in range(len(grid)):
        for c in range(len(grid)):
            size = exploreSize(grid,r,c,visited)
            if (size >0 and count > size):
                count = size

    return count


def exploreSize(grid,r,c,visited):
    RowInbound = ((0 <= r) and (r < len(grid)))
    ColInbound = ((0 <= c) and (c < len(grid)))

    if (not RowInbound or not ColInbound):
        return 0
    if (grid[r][c] == 'W'):
        return 0
    pos = str(r)+','+str(c)
    if pos in visited:
        return 0
    visited.append(pos)
    size = 1
    size += exploreSize(grid, r-1, c, visited)
    size += exploreSize(grid, r+1, c, visited)
    size += exploreSize(grid, r, c-1, visited)
    size += exploreSize(grid, r, c+1, visited)
    return size




w = [
    ['W','L','W','W','W'],
    ['W','L','W','W','W'],
    ['W','W','W','L','W'],
    ['W','W','L','L','W'],
    ['L','W','W','L','L'],


]

print(minimum(w))