import numpy as np

class ListGenerator():
    def __init__(self, seed: int = 42):
        self.seed = seed
        self.generated_list = []
    
    # Función que genera la lista de ints
    def generate_list(self, length: int):

        # Generamos una lista de valores aleatorios entre 0 y 100 de tamaño "length"
        array = np.random.randint(0, 100, size = length)

        # Pasamos la lista de "numpy.ndarray" a "list"
        array = array.tolist()

        # Guardamos la array generada
        self.generated_list = array

    # Función que devuelve la lista
    def get_list(self):
        return self.generated_list

