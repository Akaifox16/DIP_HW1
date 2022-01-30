from gaussian import gaussianElimination
from segment import generateDistGrid, generateExpectedGrid
from interpolation import nearestNeighborInterpolation
from numpy.linalg import solve

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
    abcd, efgh = findLinearFunction(exs, eys, dxs, dys)
    for y in range(y_init, y_end+1):
        for x in range(x_init, x_end+1):
            x_prime = round(find_coordinate(abcd, x, y), 3)
            y_prime = round(find_coordinate(efgh, x, y), 3)
            # print(x, y)
            oo, oi, io ,ii = getNeighbor(x, y, distimage)
            neighbor = [[oo, oi],[io, ii]]
            image[x][y] = nearestNeighborInterpolation(neighbor, x_prime, y_prime)
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
    origin = [[ dist_xs[i], dist_ys[i], dist_xs[i]*dist_ys[i], 1] for i in range(3,-1, -1)]
    xs = [expected_xs[i] for i in range(3, -1, -1)]
    ys = [expected_ys[i] for i in range(3, -1, -1)]

    a, b, c, d = solve(origin, xs)
    # print(a, b, c, d)
    e, f, g, h = solve(origin, ys)
    # print(e, f, g, h)
    return  [a, b, c, d] , [e, f, g, h]

def find_coordinate( coeff, x, y):
    a, b, c, d = [round(x,2) for x in coeff]
    return a*x + b*y + c*x*y + d 