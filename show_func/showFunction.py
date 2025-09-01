import matplotlib.pyplot as plt
import base64
from io import BytesIO

class ShowFunction:
    def __init__(self, values_x, values_y):
        self.values_x   = values_x
        self.values_y   = values_y
        self.fig, self.ax = plt.subplots()

    def custom_labels(self, title, name_xlabel, name_ylabel) -> None:

        self.ax.plot(self.values_x, self.values_y, ',:m', label=f"Fuction {title}")
        #self.plt.plot(self. values_x, self.values_y)
        
        self.ax.set_ylabel(name_ylabel)
        self.ax.set_xlabel(name_xlabel)
        self.ax.set_title(f"Gráfica del {title}")
        self.ax.grid(visible=True, axis='both')
        self.ax.legend()

    def get_image(self):
        #Guardamos la imagen en un buffer (BytesIO)
        buffer = BytesIO()
        self.fig.savefig(buffer, format = 'png')
        buffer.seek(0)

        #Convertir la imagen a base64 para pasar
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()

        #Con esos metodos nos aseguramos de limpiar la figura para que no se sobrescriba
        self.fig.clf()
        #self.fig.close() #Puede ser none y automaticamente se limpia el mismo
        return image_base64

    

    
