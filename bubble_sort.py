class BubbleSortAlgorithm():

    # Función constructor
    def __init__(self, array: list = [5, 8, 1, 9, 7]):
        self.array = array

    # Función de print
    def __str__(self):
        return str(self.array)

    # Función de devuelve la lista
    def get_list(self):
        return self.array

    # Bubble sort
    def sort(self):

        # Guardamos el tamaño de la lista
        n_elements: int = len(self.array)

        # Guardamos la lista en una variable temporal
        elements: list = self.array

        # Recorremos toda la lista
        for i in range(n_elements):

            swapped = False

            for j in range(0, n_elements - i - 1):

                # Miramos si el número actual es mayor al que tiene después
                if elements[j] != elements[j+1]:
                    if elements[j] < elements[j+1]:
                        # Hacemos swap de los valores
                        elements[j], elements[j+1] = elements[j+1], elements[j]

                        # Indicamos que se ha hecho un cambio
                        swapped = True

            if not swapped: break

        self.array = elements
