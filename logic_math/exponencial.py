from mathfunction import MathFunction

class Exponencial(MathFunction):
    """Clase de la funcion Expoencial que lo emula"""

    def calculate(self, x_values):
        return self.np.exp(x_values)