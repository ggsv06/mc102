import math
import latexify
import sympy as sp



@latexify.function
def Ua():
    t = sp.symbols('t')
    ut = sp.symbols('ut')
    h = sp.symbols('h')
    uh = sp.symbols('uh')
    f = ( 2/(t**2) )*(( (uh**2) + 4*(((h*uh)/t)**2) )**(1/2))
    return f

def Ut(g, r, ur, a, ua, b, ub):
    f = (g/(a))*(( ((r*ub)**2) + (((b*r*ua)/a)**2) + ((b*ur)**2) )**(1/2))
    return f

def Ui(g, m, um, r, ur, a, ua):
    f = (g*r)*(( ((2*ur*((1/a) - m))**2) + (( (r*ua)/(a**2) )**2) + ((r*um)**2) )**(1/2))
    return f

print(Ua)
