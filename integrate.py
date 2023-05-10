from abc import ABC, abstractmethod
import scipy
import math


class Integrator(ABC):

    def __call__(self, f, x1, x2):
        return self.integrate(f, x1, x2)

    @abstractmethod
    def integrate(self, f, x1 : float, x2 : float) -> float:
        pass
    

class Trapezoidal(Integrator):

    def __init__(self, step : float):
        self.step = step

    def integrate(self, f, x1: float, x2: float) -> float:
        
        result = f(x1) + f(x2)

        xi = x1 + self.step
        while xi < x2:
            result += 2 * f(xi)
            xi += self.step

        result *= self.step/2

        return result


class TrapezoidalSingularity(Integrator):

    def __init__(self, step : float):
        self.step = step

    def integrate(self, f, x1: float, x2: float) -> float:
        
        result = 0

        try:
            result += f(x1)
        except Exception:
            result += f(x1 + self.step)
        
        try:
            result += f(x2)
        except Exception:
            result += f(x2 + self.step)

        xi = x1 + self.step
        while xi < x2:
            result += 2 * f(xi)    
            xi += self.step

        result *= self.step/2

        return result


class TanhSinhQuadrature(Integrator):

    def __init__(self, step : float):
        self.step = step
        self.a = -100
        self.b = 100

    def integrate(self, f, x1: float, x2: float) -> float:
        print("HERE")

        f_transform_fit = lambda x : f(x * (x2-x1)/2 + (x1+x2)/2)
        result = 0

        f_transform_tanhsinh = lambda k : f(math.tanh(0.5 * math.pi * math.sinh(k * self.step)))

        w = lambda k : 0.5 * self.step * math.pi * math.cosh(k * self.step) / math.cosh(0.5 * math.pi * math.sinh(k * self.step))**2

        result = 0
        for k in range(self.a, self.b):
            result += w(k) * f_transform_tanhsinh(k)

        result *= (x2-x1) / 2

        print("HERE")
        return result



if __name__=="__main__":

    integrator = TrapezoidalSingularity(0.0001)
    f = lambda x : math.sin(x**2)
    result = integrator(f, 0, 2)
    print(result)

    print(scipy.integrate.quad(f, 0, 2))