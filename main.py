from list_generator import ListGenerator

if __name__ == "__main__":

    answer: str = input("How long do you want the array to be?")

    unsorted_list: list = [2, 5, 6, 81, 2, 4, 8, 2, 1]

    for i in range(len(unsorted_list)):
        swapped = False
        for j in range(0, len(unsorted_list) - i - 1):
            if unsorted_list[j] < unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True

        if not swapped: break

    print(unsorted_list)
    
    list_gen = ListGenerator()
    list_gen.generate_list(20)