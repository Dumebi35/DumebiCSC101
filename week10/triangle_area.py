#Python Program to find the area of a triangle

#Take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

#calculate the semi-perimeter
s = (a + b + c) / 2

import cmath

#calculate the area
area2 = cmath.sqrt((s*(s-a)*(s-b)*(s-c))) 
print('The area is ',area2, 'in decimal places')
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)