from gaussian import gaussianElimination
from segment import generateDistGrid, generateExpectedGrid
from interpolation import nearestNeighborInterpolation

def fillImage(distimage, image):
    distGrid = generateDistGrid()
    expectGrid = generateExpectedGrid()
    n = len(distGrid)
    for i in range(n):
        fillSegment(distGrid[i], expectGrid[i], distimage, image)


def fillSegment(distSegment, expectSegment, distimage, image):
    exs = expectSegment.xs
    eys = expectSegment.ys
    dxs = distSegment.xs
    dys = distSegment.ys
    # print(dxs, dys)
    x_init = int(exs[0])
    x_end = int(exs[-1])
    # print(x_init, x_end)
    y_init = int(eys[0])
    y_end = int(eys[-1])
    # print(y_init, y_end)
    find_x, find_y = findLinearFunction(exs, eys, dxs, dys)
    for i in range(y_init, y_end+1):
        for j in range(x_init, x_end+1):
            x = round(find_x(j, i), 7)
            y = round(find_y(j, i), 7)
            if x - int(x) != 0 or y - int(y) != 0:
                oo, oi, io ,ii = getNeighbor(i, j, distimage)
                neighbor = [[oo, oi],[io, ii]]
                image[i][j] = nearestNeighborInterpolation(neighbor, (x, y))
            else: 
                image[i][j] = distimage[int(x)][int(y)]
            # print(image[i][j])


def getNeighbor(i, j, distimage):
    if i+1 > 255 :
        ip = i
        i = i-1
    else:
        ip = i + 1
    if j + 1 > 255:
        jp = j
        j = j - 1
    else: 
        jp = j + 1
    oo = distimage[i][j]
    oi = distimage[i][jp]
    io = distimage[ip][j]
    ii = distimage[ip][jp]
    return oo, oi, io, ii
    
def findLinearFunction( expected_xs, expected_ys,
                        dist_xs, dist_ys ):
    pairs = []
    for i in range(4):
        pairs.append((expected_xs[i], expected_ys[i]))
    origin = [[ x, y, x*y, 1] for (x,y) in pairs]
    a, b, c, d = gaussianElimination(origin, dist_xs)
    # print(a, b, c, d)
    e, f, g, h = gaussianElimination(origin, dist_ys)
    # print(e, f, g, h)
    return  (lambda x, y: a*x + b*y + c*x*y + d) , (lambda x, y: e*x + f*y + g*x*y + h)