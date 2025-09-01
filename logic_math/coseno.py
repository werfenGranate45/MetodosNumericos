from .mathfunction import MathFunction

class Coseno(MathFunction):
    """Clase que calcula todo lo de la funcion del coseno"""
    
    def calculate(self, x_values):
        return self.np.cos(x_values)