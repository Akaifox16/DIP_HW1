def gaussianElimination(a_origin,b_origin):
    a = []
    for l in a_origin:
        a.insert(0,l.copy())
    b = []
    for l in b_origin:
        b.insert(0, l)

    x = [0,0,0,0]
    for k in range(3):
        for i in range(k+1, 4):
            r = round(a[i][k] / a[k][k], 7)
            for j in range(k+1, 4):
                a[i][j] -= r*a[k][j]
            b[i] -= r*b[k]

    for i in range(3, -1, -1):
        sum = 0
        for j in range(i+1, 4):
            sum += a[i][j]*x[j]
        x[i] = round((b[i]-sum)/a[i][i], 7)
    return x