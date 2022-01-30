def avgRGB(r,g,b,area):
    w, h = area
    avg = []
    for i in range(h):
        for j in range(w):
            sum = r[i][j] + g[i][j] + b[i][j]
            avg.append(int(sum/3))
    return avg

def diffRB(r,b, area):
    w, h = area
    drb = []
    for i in range(h):
        for j in range(w):
            diff = r[i][j] - b[i][j]
            if diff > 0 :
                drb.append(diff)
            else:
                drb.append(0)
    return drb

def excessG(r,g,b,area):
    w, h = area
    xG = []
    for i in range(h):
        for j in range(w):
            excess = 2*g[i][j] - r[i][j] - b[i][j]
            if excess >= 0 and excess <= 255:
                xG.append(excess)
            elif excess > 255:
                xG.append(255)
            else:
                xG.append(0)
    return xG