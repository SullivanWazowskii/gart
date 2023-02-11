
def rotate(point, center):
    xc = 500
    yc = 500
    rotate = 90 * math.pi/180
    x1 = (x0 - xc) * math.cos(rotate) - (y0 - yc) * math.sin(rotate) + xc
    y1 = (x0 - xc) * math.sin(rotate) + (y0 - yc) * math.cos(rotate) + yc