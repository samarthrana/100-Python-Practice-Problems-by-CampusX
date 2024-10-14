# Given two rectangles, find if the given two rectangles overlap or not. 
# A rectangle is denoted by providing the x and y coordinates of two points: 
# the left top corner and the right bottom corner of the rectangle. 
# Two rectangles sharing a side are considered overlapping. 
# (L1 and R1 are the extreme points of the first rectangle and 
# L2 and R2 are the extreme points of the second rectangle).

class POint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def do_overlap( l1, r1, l2, r2):

        # for zero area
        if l1.x == r1.x or l2.x == r2.x or l1.y == r1.y or l2.y == r2.y:
            return False

        # for left of left edge case
        if l1.x > r2.x or l2.x > r2.x:
            return False

        #for above
        if r1.y > l2.y or r2.y > l1.y:
            return False

        return True

        

