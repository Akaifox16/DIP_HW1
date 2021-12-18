def objImage(grayVal,img):
    objImg = []
    for r in img:
        row = []
        for pixel in r:
            if pixel == grayVal:
                row.append(1)
            else:
                row.append(0)
        objImg.append(row)
    return objImg

def m(p, q, img):
    w = len(img[0])
    h = len(img)
    sum = 0
    for y in range(h):
        for x in range(w):
            sum += x**p * y**q * img[y][x]
    return sum

def mu(p, q,img):
    m00 = m(0,0, img)
    x0 = round(m(1,0, img)/m00 , 7)
    y0 = round(m(0,1, img)/m00 , 7)

    w = len(img[0])
    h = len(img)
    sum = 0
    for y in range(h):
        for x in range(w):
            sum += (x-x0)**p * (y-y0)**q * img[y][x]
    return round(sum, 7)

def eta(p, q, img):
    power = round((p+q)/2 + 1 , 7)
    return round(mu(p,q,img) / (mu(0,0,img) ** power) , 7)

def phi(img):
    return round(eta(2,0,img) + eta(0,2,img) , 3)