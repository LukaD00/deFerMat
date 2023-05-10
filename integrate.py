
class Trapezoidal:

    def __init__(self, step : float):
        self.step = step

    def __call__(self, f, x1, x2):
        return self.integrate(f, x1, x2)

    def integrate(self, f, x1: float, x2: float) -> float:
        
        result = 0

        try:
            result += f(x1)
        except Exception:
            result += f(x1 + self.step)
        
        try:
            result += f(x2)
        except Exception:
            result += f(x2 - self.step)

        xi = x1 + self.step
        while xi < x2:
            result += 2 * f(xi)    
            xi += self.step

        result *= self.step/2

        return result

