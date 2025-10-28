from list_generator import ListGenerator

if __name__ == "__main__":

    answer: str = input("How long do you want the array to be? ")
    
    list_gen = ListGenerator()
    list_gen.generate_list(int(answer))

    
    unsorted_list: list = list_gen.get_list()

    for i in range(len(unsorted_list)):
        swapped = False
        for j in range(0, len(unsorted_list) - i - 1):
            if unsorted_list[j] < unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True

        if not swapped: break

    print(unsorted_list)
    
    