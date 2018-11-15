class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

def minimumDistance(numRows, numColumns, area):
    # WRITE YOUR CODE HERE
    start = Point(0,0)
    destination = 
    print area

print (minimumDistance(3,3,[[1,0,0],[1,0,0],[1,9,1]]))