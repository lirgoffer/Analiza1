import math
from math import e
import sympy as sp
import math
from sympy.utilities.lambdify import lambdify

x = sp.symbols('x')


def TrapezoidalRule(f, n, a, b, tf):
    """
    rapezoidal Rule is a rule that evaluates the area under the curves by dividing the total area
    into smaller trapezoids rather than using rectangles
    :param f: The desired integral function
    :param n: The division number
    :param a: Lower bound
    :param b: Upper bound
    :param tf: Variable to decide whether to perform Error evaluation
    :return: The result of the integral calculation
    """
    h = (b - a) / n
    if tf:
        print("Error evaluation En = ", round(TrapezError(func(), b, a, h), 6))
    integral = 0.5 * (f(a) * f(b))
    for i in range(n):
        integral += f(a + h * i)
    integral *= h
    return integral


def SimpsonRule(f, n, a, b):
    """
    Simpson’s Rule is a numerical method that approximates the value of a definite integral by using quadratic
     functions Simpson’s Rule is based on the fact that given three points,
    we can find the equation of a quadratic through those points (by Lagrange's interpolation)
    :param f: The desired integral function
    :param n: The division number(must be even)
    :param a: Lower bound
    :param b: Upper bound
    :return: The result of the integral calculation
    """
    if n % 2 != 0:
        return 0, False
    h = (b - a) / n
    print("Error evaluation En = ", round(SimpsonError(func(), b, a, h), 6))
    integral = f(a) + f(b)
    for i in range(n):
        k = a + i * h
        if i % 2 == 0:
            integral += 2 * f(k)
        else:
            integral += 4 * f(k)
    integral *= (h / 3)
    return integral, True


def func():
    return sp.sin(x ** 2 + 5 * x +6) / (2 * sp.exp((-1) * x))


def f(val):
    return lambdify(x, func())(val)


def TrapezError(func, b, a, h):
    """
    The trapezoidal rule is a method for approximating definite integrals of functions.
    The error in approximating the integral of a twice-differentiable function by the trapezoidal rule
    is proportional to the second derivative of the function at some point in the interval.
    :param func: The desired integral function
    :param b: Upper bound
    :param a: Lower bound
    :param h: The division
    :return: The error value
    """
    xsi = (-1) * (math.pi / 2)
    print("ƒ(x): ", func)
    f2 = sp.diff(func, x, 2)
    print("ƒ'': ", f2)
    diff_2 = lambdify(x, f2)
    print("ƒ''(", xsi, ") =", diff_2(xsi))
    return h ** 2 / 12 * (b - a) * diff_2(xsi)


def SimpsonError(func, b, a, h):
    """
    The Simpson rule is a method for approximating definite integrals of functions.
    The error in approximating the integral of a four-differentiable function by the trapezoidal rule
    is proportional to the second derivative of the function at some point in the interval.
    :param func: The desired integral function
    :param b: Upper bound
    :param a: Lower bound
    :param h: The division
    :return: The error value
    """
    xsi = 1
    print("ƒ(x): ", func)
    f2 = sp.diff(func, x, 4)
    print("ƒ⁴: ", f2)
    diff_4 = lambdify(x, f2)
    print("ƒ⁴(", xsi, ") =", diff_4(xsi))

    return (math.pow(h, 4) / 180) * (b - a) * diff_4(xsi)


def MainFunction():
    n = 4
    print("Division into sections n =", n)

    choice = True
    while choice:
        print("---\n")
        choice = int(input(f"Welcome! Choose:\n"
                           "\t1. Trapezoidal Rule.\n"
                           "\t2. Simpson’s Rule.\n"
                           "\tEXIT. Click any other char.\n"
                           "---\n"))

        if choice == 1:
            print("I = ", round(TrapezoidalRule(f, n, 0, 1, True), 6))
        elif choice == 2:
            res = SimpsonRule(f, n, 0, 1)
            if res[1]:
                print("I = ", round(res[0], 6))
            else:
                print("n must be even !")
        else:
            print("Goodbye :)")
            break


MainFunction()
