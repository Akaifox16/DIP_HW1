def nearestNeighborInterpolation(neigbor, x, y):
    int_x = toInt(x)
    int_y = toInt(y)
    return neigbor[int_y][int_x]

def toInt(n):
    if n - int(n) >= 0.5:
        return  1
    else: 
        return  0