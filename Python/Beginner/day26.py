class Point(object):
    '''Creates a point object'''
    def __init__(self, x, y):
        '''Initialises the onject'''
        self.x = x
        self.y = y

    def __repr__(self):
        '''String representation'''
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        '''Adds two point objects together'''
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''Subtracts two point objects together'''
        return Point(self.x - other.x, self.y - other.y) 

    def __mul__(self, other):   
        '''Multiplies two point objects together'''
        if isinstance(other, Point):
            return (other.x * self.x) + (other.y * self.y)
        elif isinstance(other, int):
            
            return Point(other * self.x, other * self.y)
        
    def distance(self, other):
        '''Computes the exclidean distance between two point objects together'''
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**0.5

2*Point(4, 7).__mul__(Point(5, 6))==124 # 2 points
round(Point(1, 4).__add__(Point(4, 6)).__sub__(Point(1, 3)).distance(Point(3, 5)), 5)==2.23607 # 3 points
Point(3, 6).__add__(Point(5, 7)).__mul__(Point(1, 4).__add__(Point(5, 6)))==178 # 2 points
round(Point(-1, 5).distance(Point(6, 4).__mul__(2)), 5)==13.34166 # 2 points
Point(0.5, 7).__mul__(Point(2, 5))==36.0 # 2 points
round((Point(1, 2).__add__(Point(3, 5))).distance(Point(100, 4.6).__sub__(Point(1, 50))), 1)==108.5 # 3 points