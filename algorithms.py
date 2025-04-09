import numpy as np # for randomized arrays

class Algorithm:
    
    # pseudo-code
    # for every element in array - 1 (avoid out of bounds)
    #   compare current element to next element
    #   iterate for length of array - 1 - amount of elements already sorted
    #       if current element is greater than next, swap them
    # array is now sorted in ascending order so it can be returned
    
    @staticmethod
    def bubble(array: list) -> list:
        for elem in range(len(array) - 1):
            for unsorted in range(len(array) - elem - 1):
                if array[unsorted] > array[unsorted + 1]:
                    Algorithm.swap(array, unsorted, unsorted + 1)
        return array

    # This algorithms time complexity is O(n^2). The reason for this,
    # the outer loop and inner loop have n in their range. This means
    # we loosely loop n times for every n -> n*n. Although the actual loop counts
    # differ (the iterations of the inner decrement according to already
    # sorted elements), what matters is n is used as the variable in
    # each loop. This is why it is O(n^2)


    # Psuedo code for insertion sort
    
    @staticmethod
    def insertion(array: list) -> list:
        for elem in range(1, len(array)):
            for unsorted in range(elem):
                if array[elem - unsorted] > array[elem - unsorted - 1]:
                    break
                Algorithm.swap(array, elem - unsorted, elem - unsorted - 1)
        return array
    
    # Big O for insertion sort
    
    
    # Psuedo code for selection sort
    
    @staticmethod
    def selection(array: list) -> list:
        for elem in range(len(array)):
            lowest_value_idx = elem
            for unsorted in range(elem, len(array)):
                if array[unsorted] < array[lowest_value_idx]:
                    lowest_value_idx = unsorted
            Algorithm.swap(array, lowest_value_idx, elem)
        return array
    
    # Big O for selection sort
    
    
    @staticmethod
    def swap(array: list, idx1, idx2):
        array[idx1], array[idx2] = array[idx2], array[idx1]


if __name__ == "__main__":
    # for _ in range(100):
    #     arr = np.random.randint(100, size=(np.random.randint(0, 100)))
    #     Algorithm.selection(arr)
    Algorithm.swap([1], 0, 1)