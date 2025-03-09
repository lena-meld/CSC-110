'''
Magdalena Sammut
CSC 110-002
Project -1
This script contains four functions:
    The first function takes two arguments, base and height,
    to calculate the area of a rectangle. The area is 
    calculated by multiplying the base by the height.
    The second function takes three arguments--a, b, and c--
    to calculate the area of a triangle using Heron's Formula.
    The semiperimeter is first calculated, then used with the 
    arguments to find the area of a triangle.
    The third function also takes three arguments--base_1, base_2,
    and height-- to calculate the area of a trapezoid. The sum of
    base_1 and base_2 are multiplied by the height, and this result
    is divided by two.
    The final function takes one argument, radius, to calculate
    the area of a circle rounded to two decimal places. The area is
    found by squaring the radius and multiplying by pi, where pi is
    equal to 3.1415. 
    All four functions return a float.
'''

def rectangle_area(base,height):
    '''
    This function calculates the area of a rectangle by
    multiplying the first argument, base, by the second
    argument, height
    Args:
        base: a float representing the base of a
        rectangle
        height: a float representing the height
        of a rectangle
    Return:
        The calculated area of a rectangle as a float
    '''
    # calculate the area of a rectangle
    r = base * height
    # return area of the rectangle
    return(r)

def triangle_area(a,b,c):
    '''
    This function calculates the area of a triangle
    accroding to Heron's formula. It therefore accepts
    three arguments: a, b, and c. Each of these
    arguments correspond to one side of the triangle.
    To use Heron's formula, however, the semi perimeter
    of the triangle must first be calculated by adding
    up the sides and diving the result by two
    Args:
        a: a float representing one side of a triangle
        b: a float representing another side of a triangle
        c: a float representing the last side of the
        triangle
    Return:
        The calculated area of a triangle as a float
    '''
    # calculate the semiperimeter of the triangle
    s = (a+b+c)/2
    # calculate the area of the triangle
    t = (s*(s-a)*(s-b)*(s-c))**(1/2)
    # return area of the triangle
    return(t)

def trapezoid_area(base_1,base_2, height):
    '''
    This function calculates the area of a trapezoid.
    It accepts three arguments: base_1, base_2, and height.
    base_1 represents one parallel segment of the trapezoid
    and base_2 represents the other. height represents the 
    height of the shape. The height multiplied by the sum of
    base_1 and base_2 of the trapezoid all divided by two
    will give the area of the trapezoid
    Args:
        base_1: a float representing one side of the
        trapezoid
        base_2: a float representing the side of the trapezoid
        parallel to base_1
        height: a float representing the height of the trapezoid
    Return:
        The calculated area of a trapezoid as a float
    '''
    # calculate the area of the trapezoid
    p = ((base_1 + base_2) * height)/2
    # return the area of the trapezoid
    return(p)

def circle_area(radius):
    '''
    This function calculates the area of a circle rounded
    to two decimal places.
    It calculates the area by squaring the argument, 
    radius, and multiplying it by pi (3.1415)
    Arg:
        radius: a float representing the radius of the circle
        in question
    Return:
        The calculated area of a circle as a float
    '''
    # calculate the area of the circle
    c = 3.1415 * (radius)**2
    # return the rounded area of the circle
    return(round(c,2))

