class info_gather:

    '''
    color:
        g = green
        p = purple
        o = orange

    opacity:
        100 = solid
        50 = half shaded
        0 = hollow

    num:
        1 = 1 of shape
        2 = 2 of shape
        3 = 3 of shape
    '''

    def __init__(self, color, opacity, num):
        self.color = color
        self.opacity = opacity
        self.num = num

    def printtest(self):
        print(self.color, self.opacity, self.num)

def compare(color1, opacity1, num1, color2, opacity2, num2, color3, opacity3, num3):
    
    if color1 != color2 and color2 != color3 and color1 != color3:
        print('color diff')
        color_same = True
    else:
        print('color same')
        color_same = False

    if opacity1 != opacity2 and opacity2 != opacity3 and opacity1 != opacity3:
        print('opac diff')
        opac_same = True
    else:
        print('opac same')
        opac_same = False

    if num1 != num2 and num2 != num3 and num1 != num3:
        print('num diff')
        num_same = True
    else:
        print('num same')
        num_same = False

s1 = info_gather("g", 100, 1)
s1.printtest()

s2 = info_gather("p", 0, 1)
s2.printtest()

s3 = info_gather("o", 50, 1)
s3.printtest()

compare(s1.color, s1.opacity, s1.num, s2.color, s2.opacity, s2.num, s3.color, s3.opacity, s3.num)