import math as m
import latexify
import sympy as sp


@latexify.function
def Ua(t, ut, h, uh):
    return ( 2/(t**2) )*(m.sqrt( (uh**2) + 4*(((h*ut)/t)**2) ))
    
@latexify.function
def Ut(g, r, ur, a, ua, b, ub):
    return ( (g)/(a) )*m.sqrt(((r*ub)**2) + ((b*r*ua/a)**2) + ((b*ur)**2))
   
@latexify.function
def Ui(g, m, um, r, ur, a, ua):
    return (g*r)*m.sqrt( ((2*ur*((1/a) - m))**2) + (( (r*ua)/(a**2) )**2) + ((r*um)**2) )

# @latexify.function
#     def Uiesp

print(f'{Ua}\n') 
print(f'{Ut}\n')
print(f'{Ui}\n')