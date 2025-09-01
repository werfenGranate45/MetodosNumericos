"""
Este modulo se encarga de englobar todas las necesidades logicas que desamos
para la app de CalculatorAPP, entre clases, metodos o atributos
"""

from logic_math.coseno  import Coseno
from logic_math.seno import Seno 
from logic_math.exponencial import Exponencial 

def match_operation(name_operation, numero):
    """
    Esta metodo se encarga de hacer el match la operacion
    y regresar el resultado calculandolo con su numero dado

    >>> name_operation: Nombre de la operacion
    >>> numero: Numero con el que se va Calcular
    """
    sen, cos, exp = Seno(), Coseno(), Exponencial()
    x_value , y_value = None, None
    
    match name_operation:
      case 'sen':
        x_value = sen.preparate_x_values(numero)
        y_value = sen.calculate(x_value)
      case 'cos': 
        x_value = cos.preparate_x_values(numero)
        y_value = cos.calculate(x_value)
      case 'exp': 
        x_value = exp.preparate_x_values(numero)
        y_value = exp.calculate(x_value)
      case _:
          return None

    return x_value , y_value