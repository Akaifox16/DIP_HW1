class Segment:
    def __init__(self,xs,ys):
        self.xs = xs
        self.ys = ys
    
def generateExpectedGrid():
    segments = []
    for y in range(0,256,16):
        for x in range(0,256,16):
            xp = x + 16 if x + 16 < 256 else 255
            yp = y + 16 if y + 16 < 256 else 255
            xs = [x,xp,x,xp]
            ys = [y,y,yp,yp]
            segments.append(Segment(xs,ys))
    return segments

def generateDistGrid():
    segments = []
    file = open('/home/akaifox/_workspace/DIP/distSegment.txt','r')
    for _ in range(256):
        xs = [int(x) for x in file.readline().split()]
        ys = [int(y) for y in file.readline().split()]
        segments.append(Segment(xs,ys))
    return segments