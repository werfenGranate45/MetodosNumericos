from mathfunction import MathFunction

class Seno(MathFunction):
    """Clase que Calcula la funcion seno, como x en argumento, y la funcion"""

    def calculate(self, x_values):
        return self.np.sin(x_values)
