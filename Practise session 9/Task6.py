import math
class Point:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def distance(self):
        x=self.x2-self.x1
        y=self.y2-self.y1
        result=math.sqrt((x*x)+(y*y))
        print(result)
p1=Point(3,7,4,1)
p1.distance()