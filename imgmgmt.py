def flatten(ls):
    flat = []
    for r in ls:
        for x in r:
            flat.append(x)
    return flat

def findObjectGrayScale(img):
    objGray = []
    unique = findUniqueValue(img)
    flat = flatten(img)
    for val in unique:
        if flat.count(val) > 2000:
            objGray.append(val)
    return objGray

def findUniqueValue(img):
    unique = []
    for row in img:
        for x in row:
            if x != 255 and x not in unique:
                unique.append(x)
    return unique

def hist(flatImg):
    return [flatImg.count(i) for i in range(256)]