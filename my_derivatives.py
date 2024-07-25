import sympy as sym
x = sym.Symbol('x')
func = x**4+4*x**2+5*x-6
sym.Derivative(func, x)