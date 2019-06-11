class Solution:

    def __init__(self, radius, x_center, y_center):
        self.x_r = [x_center-radius,x_center+radius]
        self.y_r = [y_center-radius,y_center+radius]
        self.x_c = x_center
        self.y_c = y_center
        self.r = radius

    def randPoint(self):
        while True:
            x = random.uniform(self.x_r[0],self.x_r[1])
            y = random.uniform(self.y_r[0],self.y_r[1])
            if (x-self.x_c)**2+(y-self.y_c)**2<=self.r**2:
                return [x,y]
