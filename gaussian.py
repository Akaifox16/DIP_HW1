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