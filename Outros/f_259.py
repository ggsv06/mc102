import math as m
import latexify
import sympy as sp


g = 9.8
r = 0.05
ur = 10**(-5)
a = 3.6
ua = 0.3
b = -0.06
ub = 0.03
mp = 2.02350
mass = 1.928
um = 0.0003*m.sqrt(2)
t = [3.91, 3.3, 2.1, 1.5, 2, 5]
ut = 0.01
h = 0.868
uh = 2*10**(-4)


def Ua(t, ut, h, uh):
    return ( 2/(t**2) )*(( (uh**2) + 4*(((h*ut)/t)**2) )**(1/2))
    

def Ut(g, r, ur, a, ua, b, ub):
    return ( (g)/(a) )*m.sqrt(((r*ub)**2) + ((b*r*ua/a)**2) + ((b*ur)**2))
   

def Ui(g, m, um, r, ur, a, ua):
    return (g*r)*( ((2*ur*((1/a) - m))**2) + (( (r*ua)/(a**2) )**2) + ((r*um)**2) )**(1/2)

def Uiesp(ur, mp, r):
    return ur*mp*r


print(f'Ui = {Ui(g, mass, um, r, ur, a, ua)}')
print(f'Ut = {Ut(g, r, ur, a, ua, b, ub)}')
print(f'UIesp = {Uiesp(ur, mp, r)}')

print('\nUa')
for j, i in enumerate(t):
    print(f'{j+1}\t{Ua(i, ut, h, uh)}')