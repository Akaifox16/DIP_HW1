def gaussianElimination(a_origin, b):
    a = a_origin.copy()

    x = [0,0,0,0]
    for k in range(3):
        for i in range(k+1, 4):
            if a[k][k] <= 0:
                print(a)
            r = a[i][k] / a[k][k]
            for j in range(k+1, 4):
                a[i][j] -= r*a[k][j]
            b[i] -= r*b[k]

    for i in range(-1, -5, -1):
        sum = 0
        for j in range(i+1, 4):
            sum += a[i][j]*x[j]
        x[i] = (b[i]-sum)/a[i][i]

    return x

def createMat3(i,j, a):
    ans = []
    for r in range(4):
        row = []
        if r == i:
            continue
        for c in range(4):
            if c == j:
                continue
            row.append(a[r][c])
        ans.append(row)
    return ans

def det4(a):
    d00 = a[0][0]*det3(createMat3(0,0,a))
    d10 = a[1][0]*det3(createMat3(1,0,a))
    d20 = a[2][0]*det3(createMat3(2,0,a))
    d30 = a[3][0]*det3(createMat3(3,0,a))
    return d00 -d10 +d20 -d30

def det3(a):
    up = a[0][0]*a[1][1]*a[2][2]
    up += a[0][1]*a[1][2]*a[2][0] 
    up += a[0][2]*a[1][0]*a[2][0] 
    down = a[2][0]*a[1][1]*a[0][2]
    down += a[2][1]*a[1][2]*a[0][0]
    down += a[2][2]*a[1][0]*a[0][1]
    return up - down

def createCramerMat(i, a, b):
    ans = a.copy()
    for idx, number in enumerate(b) :
        ans[idx][i] = number
    return ans

def cramer(a, b):
    d = det4(a)
    print(d)
    ai = [createCramerMat(i, a, b) for i in range(4)]
    return [det4(mat)/d for mat in ai]