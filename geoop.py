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
    x_range = range(int(exs[0]), int(exs[-1]))
    y_range = range(int(eys[0]), int(eys[-1]))
    abcd, efgh = findLinearFunction(exs, eys, dxs, dys)
    for y in y_range:
        for x in  x_range:
            y_prime = find_coordinate(abcd, x, y)
            x_prime = find_coordinate(efgh, x, y)
            oo, oi, io ,ii = getNeighbor(int(x_prime), int(y_prime), distimage)
            image[y][x] = nearestNeighborInterpolation([[oo, oi],[io, ii]], x_prime, y_prime)

def getNeighbor(i, j, distimage):
    oo = distimage[i][j]
    oi = distimage[i][j+1] if j + 1 < 256 else 0 
    io = distimage[i+1][j] if i + 1 < 256 else 0
    ii = distimage[i+1][j+1] if j +1 < 256 and i +1 < 256 else 0
    return oo, oi, io, ii
    
def findLinearFunction( expected_xs, expected_ys,
                        dist_xs, dist_ys ):
    origin = [[ expected_xs[i], expected_ys[i], expected_xs[i]*expected_ys[i], 1] for i in range(-1,-5,-1)]
    xs = [dist_xs[i] for i in range(-1, -5, -1)]
    ys = [dist_ys[i] for i in range(-1, -5, -1)]

    a, b, c, d = solve(origin, xs)
    e, f, g, h = solve(origin, ys)
    return  [a, b, c, d] , [e, f, g, h]

def find_coordinate( coeff, x, y):
    a, b, c, d = coeff
    return a*x + b*y + c*x*y + d 