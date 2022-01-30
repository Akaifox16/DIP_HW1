from imgmgmt import flatten

def contrastStretching(img):
    flatImg = flatten(img)
    min_gray = min(flatImg)
    diff_gray = max(flatImg) - min_gray
    w = len(img[0])
    h = len(img)
    for r in range(h):
        for c in range(w):
            img[r][c] = int((img[r][c] - min_gray) / diff_gray * 255)
    return w, h