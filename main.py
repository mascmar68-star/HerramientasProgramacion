from list_generator import ListGenerator
from bubble_sort import BubbleSortAlgorithm

if __name__ == "__main__":

    # Preguntamos al usuario que dimensión de lista quiere
    answer: str = input("\n\n¿Qué tamaño de lista quieres? ")

    # Creamos un generador de listas
    list_gen = ListGenerator()
    list_gen.generate_list(int(answer))

    # Mostramos la lista aleatoria generada
    print(f"\nLista inicial (desordenada): {list_gen}")

    # Guardamos la lista generada
    unsorted_list: list = list_gen.get_list()

    # Creamos un BubbleSort
    sorting_algorithm = BubbleSortAlgorithm(array=unsorted_list)

    # Aplicamos BubbleSort
    sorting_algorithm.sort()

    # Mostramos el resultado final
    print(f"Lista final (ordenada): {sorting_algorithm}\n\n")
