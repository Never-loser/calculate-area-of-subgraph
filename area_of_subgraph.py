import sympy as sp

x = sp.Symbol('x')
f_expr = 3 ** x + 1
a, b = 0.1, 1
n = 10


def simpsons_rule(f_num, a, b, n):


    if n % 2 != 0:
        raise ValueError("The number of divisions of n must be even.")
    h = (b - a) / n
    result = f_num(a) + f_num(b)
    for i in range(1, n):
        x_i = a + i * h
        result += 4 * f_num(x_i) if i % 2 != 0 else 2 * f_num(x_i)
    return (h / 3) * result


def smart_integrate(f_expr, a, b, n=10):


    x = sp.Symbol('x')
    integral_expr = sp.integrate(f_expr, (x, a, b))
    if integral_expr.has(sp.Integral):
        print("The analytical integral is not simple. Using Simpson's rule...")
        f_num = sp.lambdify(x, f_expr, 'math')
        return simpsons_rule(f_num, a, b, n)
    else:
        try:
            numeric_result = float(integral_expr.evalf())
            print("The analytical integral was simple. The exact answer is:")
            return numeric_result
        except:
            print("Error in numerical calculation! Using Simpson's rule...")
            f_num = sp.lambdify(x, f_expr, 'math')
            return simpsons_rule(f_num, a, b, n)
result = smart_integrate(f_expr, a, b, n)
print(f"\n Final value of the integral from 0 to 1: {result}")
