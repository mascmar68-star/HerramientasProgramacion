class BubbleSortAlgorithm():

    # Función constructor
    def __init__(self, array: list = [5, 8, 1, 9, 7]):
        self.array = array

    def __str__(self):
        return str(self.array)

    def sort(self):

        for i in range(len(self.array)):
            swapped = False
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] < self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    swapped = True

            if not swapped: break

        print(self.array)


