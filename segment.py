class Segment:
    def __init__(self,xs,ys):
        self.xs = xs
        self.ys = ys
    
def generateExpectedGrid():
    segments = []
    for y in range(0,256,16):
        for x in range(0,256,16):
            xs = [x,x+15,x,x+15]
            ys = [y,y,y+15,y+15]
            # print(xs, ys)
            segment = Segment(xs,ys)
            segments.append(segment)
    # print(len(segments))
    return segments

def generateDistGrid():
    segments = []
    file = open('/home/akaifox/_workspace/DIP/distSegment.txt','r')
    for _ in range(256):
        xs = [int(x) for x in file.readline().split()]
        ys = [int(y) for y in file.readline().split()]
        segments.append(Segment(xs,ys))
    return segments