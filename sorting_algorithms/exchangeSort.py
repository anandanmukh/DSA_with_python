def exchangeSort(array, *args):
    """
    Sorts the input array using the Exchange Sort Algorithm.

    Exchange Sort is a simple sorting algorithm that repeatedly swaps adjacent elements 
    in the array if they are in the wrong order. The algorithm iterates through 
    the array multiple times, comparing adjacent elements and swapping them if
    they are in the wrong order. Each iteration moves the smallest unsorted element 
    to its correct position in the sorted portion of the array.

    Args:
        array (list): The unsorted input array.

    Yields:
        tuple: A tuple containing the current state of the array and the indices of 
        the elements being compared in the current iteration.
    """
    size = len(array)
    for i in range(size - 1):
        for j in range(i + 1, size):
            yield array, i, j, -1, -1
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]


if __name__ == "__main__":
    import random
    array = [random.randint(0, 100) for i in range(10)]

    # print the array before and after sorting
    print(f'The unsorted array: {array}')

    exchangeSort(array, array[0], array[-1])
    print(f"The sorted array: {array}")