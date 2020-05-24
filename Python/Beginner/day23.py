class circle:
    ''''''
    def __init__(self, radius):
        self.radius = radius
    
    def computeCircum(self):
        return f'{int(round(2 * 22/7 * self.radius, 0))}cm'
        
    def computeArea(self):
        return f'{int(round(22/7*self.radius**2, 0))}cm2'

print(circle(7).computeArea() =='154cm2')# 3 points
print(circle(7).computeCircum() =='44cm')# 3 points
print(circle(7).__doc__!=None) # 1 point

print(circle(7.5).radius ==7.5)# 1 point
print(circle(7.5).computeCircum()=='47cm') #3  points
print(circle(7.5).computeArea()=='177cm2')# 3 points

