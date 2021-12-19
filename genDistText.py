import json

with open('dist.json') as json_file:
    data = json.load(json_file)

    with open('distSegment.txt','w') as segment_file:
        for seg in data:
            segment_file.write('{} {} {} {}\n'.format(seg['x1'], seg['x2'], seg['x3'], seg['x4']))
            segment_file.write('{} {} {} {}\n'.format(seg['y1'], seg['y2'], seg['y3'], seg['y4']))