from abc import ABC, abstractmethod
import numpy as np

class MathFunction(ABC):
    """Contantes para el uso de calculos matematicos"""
    def __init__(self):
        self.PI    = np.pi
        self.EULER = np.e
        self.data_user = 0.0
        self.np        = np
    
    @abstractmethod
    def calculate(self, x_values):
        pass
    
    def preparate_x_values(self, prompt):
        """
        Metodo que prepara el rango de elementos de la x, en un narray
        para que pueda ser calculada por el sin, cos o exp
        """
        radians = self.degrees_to_radians(prompt)
        start = radians * 2
        end   = -start
        #Esta modificacion es usada para dar ciclos practicamente es geometria
        #En este caso esta hecho para dar 2 ciclos del comportamiento del seno
        return self.np.linspace(start, end, 200)     
      
    def degrees_to_radians(self, degrees: float):
        """Metodo que se encarga de grados a radianas"""
        return np.deg2rad(degrees)
    