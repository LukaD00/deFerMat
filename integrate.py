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



if __name__=="__main__":

    integrator = Trapezoidal(0.0001)
    f = lambda x : math.sin(x**2)
    result = integrator(f, 0, 2)
    print(result)

    print(scipy.integrate.quad(f, 0, 2))