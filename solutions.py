import math
import scipy
from integrate import Trapezoidal, TrapezoidalSingularity, TanhSinhQuadrature


def task1():
    integrator = Trapezoidal(0.0001)
    integrand = lambda t : math.sin(t**2)

    f = lambda x : integrator(integrand, 0, x)
    x = 2
    print(f(x))
    print(scipy.integrate.quad(integrand, 0, x))


def task2():
    integrator = TrapezoidalSingularity(0.0001)
    integrand = lambda t : 1 / math.sqrt(t)

    f = lambda x : integrator(integrand, 0, x)
    x = 10
    print(f(x))
    print(scipy.integrate.quad(integrand, 0, x))

    analytical = lambda x : 2 * math.sqrt(x)
    print(analytical(x))


def task3():
    integrator = TrapezoidalSingularity(0.0001)
    integrand = lambda t : -math.log(t)

    f = lambda x : integrator(integrand, 0, x)
    x = 0.5
    print(f(x))
    print(scipy.integrate.quad(integrand, 0, x))

    analytical = lambda x : x - x * math.log(x)
    print(analytical(x))


def task4():
    integrator = TrapezoidalSingularity(0.000001)
    integrand = lambda t : math.exp(t) * math.cos(t)

    f = lambda x : integrator(integrand, 0, x)
    x = 5
    print(f(x))
    print(scipy.integrate.quad(integrand, 0, x))
    
    analytical = lambda x : math.exp(x) * (math.cos(x) + math.sin(x)) / 2 - 0.5
    print(analytical(x))


def task5():
    integrator = TrapezoidalSingularity(0.00000001)
    integrand = lambda t : t**2 * math.cosh(t**2)

    f = lambda x : integrator(integrand, 0, x)
    x = 5
    print(f(x))
    print(scipy.integrate.quad(integrand, 0, x))
    
    analytical = lambda x : 0.5 * math.sinh(x**2) * (x**2 - 1) + 0.5 * math.sqrt(math.pi) * scipy.special.erf(x)
    print(analytical(x))

def task6():
    integrator = TrapezoidalSingularity(0.0000001)
    integrand = lambda t : math.sin(1/t) * math.sqrt(t) + math.cos(t)

    f = lambda x : integrator(integrand, 0, x)
    x = 2
    print(f(x))
    print(scipy.integrate.quad(integrand, 0, x))

    analytical = lambda x : math.sin(x) + (2 * math.sqrt(x) * (math.sin(1/x)*x + 2*math.cos(1/x)) + 2**(5/2) * math.sqrt(math.pi) * scipy.special.fresnel(math.sqrt(2 / (math.pi * x)))[0]) / 3
    print(analytical(x))

if __name__=="__main__":
    task6()