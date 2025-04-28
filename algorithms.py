import numpy as np # for randomized arrays
import collections as c
import datetime

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
    # Skip first element (it is sorted relative to itself)
    # From second element to the end
    # Start at the right most unsorted element
    # Compare element with element to the left (in reverse)
    # If element to the left is greater swap the two
    # If it's not greater then place the element where it is currently and go to the next iteration
    
    @staticmethod
    def insertion(array: list) -> list:
        for elem in range(1, len(array)):
            for unsorted in range(elem):
                reverse_idx = elem - unsorted
                if array[reverse_idx] > array[reverse_idx - 1]:
                    break
                Algorithm.swap(array, reverse_idx, reverse_idx - 1)
        return array
    
    # Big O for insertion sort
    # This algorithm has a different best and worst case time complexity. Its worst case is O(n^2), it best case is O(n).
    # The best case is n because the implementation has the ability to stop the sorting iterations. For an already
    # sorted array, it would break after every first comparison meaning it only does n comparisons rather than n^2 comparisons.
    # It is n^2 for the worst case because in the worst case it would go through every iteration of both loops which means n^2
    # comparisons.
    # The space complexity for insertion sort is O(1). This is because any memory allocation are deallocated after every iteration.
    # The array is returned as a copy, that is strictly a convenience to make unit testing easier, the algorithm would normally not return the array.
    
    # Psuedo code for selection sort
    # Iterate through all elements
    # Track the index of the lowest value element in current iteration
    # Iterate through all unsorted elements
    # If the element at the current iteration is less than element at tracked index, then its index is stored as the lowest index
    # At the end of the inner loop swap the lowest element with the index of the outer loops interation (implicitly tracks sorted elements)
    
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
    # The time complexity for selection sord is O(n^2). It is exponential because every outer loop iteration will have the inner loop
    # iterate for its entire given range. The range of both loops is dependent on n, hence making it O(n^2).
    # The space complexity for selection sort is O(1). This is because any memory allocation are deallocated after every iteration.
    # The array is returned as a copy, that is strictly a convenience to make unit testing easier, the algorithm would normally not return the array.
    
    
    
    # Description
    # INPUT a sorted array
    # OUTPUT the index of the element being searched for
    
    # This algorithm will guess the middle element of its given range
    # it will know if the correct element is higher than the guess or lower than the guess.
    # The incorrect portion will be eliminated from the range.
    # It will continue to guess the middle element until it is correct.
    
    # Psuedo code
    # Guess the middle element of min (0 initially) and max (array length -1 initially)
    # if it is correct, return the idx
    # if it is incorrect determine if the element is above or below the guess
    # if the element is greater than the search item than set max to the guessed index
    # if the element is less than the search item then set miin to the guess index
    # call the function again giving it the new range that the element is in until the index is found
    
    # Big-O
    # The time complexity of this algorithm is O(log(n)) because of how the algorithm works, it eliminates half of the remaining elements to search on every iteration
    # for example, if there were 16 elements, the algorithm in the worst case would eliminate 8 then 4 then 2 then 1. It found the correct element in 4 steps rather than 16
    # The space complexity for this algorithm is also O(log(n)). It would be O(1) if it weren't for the recursive nature of the algorithm. However, because it is recursive
    # every iteration is stored in memory, it iterates log(n) times so the space used is also log(n).
    
    @staticmethod
    def binary_search(search_val, array, min=0, max=0):
        if max == 0:
            max = len(array) - 1
        current_idx = (max + min) // 2
        match Algorithm.guess(search_val, array[current_idx]):
            case 1: # guess was too high
                max = current_idx
            case -1: # guess was too low
                min = current_idx + 1
            case 0:
                return current_idx
        return Algorithm.binary_search(search_val, array, min, max)
    
    @staticmethod
    def guess(target, search_guess):
        return 1 if search_guess > target else -1 if search_guess < target else 0
    
    
    # Initial evaluation
    # Input - array of comparable types
    # Output - sorted array
    # This merge will recursively walk through the array, splitting it if the size is greater than one
    # if its not of size 1 it will do the sorting process in which it walks through two arrays comparing their values and merging them accordingly
    
    # Psuedo code
    # evaluate the size of the array
    # if its size is 1 return the array so it can be compared and merged
    # if its size is not 1, split it into two arrays and call the sort for each half of the array
    # by this point we are able to do the sorting
    # call another function that takes in both broken down arrays
    # this function will use two "pointers" to track the position in the unsorted array
    # the array at those pointer locations will be compared, the lesser of which will be moved to the new array and the pointer of that lesser one will be incremented
    # once both pointers are at the end of their arrays, the array can be returned, it will be sorted
    @staticmethod
    def merge(array):
        if len(array) < 2:
            return array
        return Algorithm.combine(Algorithm.merge(array[0 : len(array) // 2]), Algorithm.merge(array[len(array) // 2 : len(array)]))
        
    @staticmethod
    def combine(arr1, arr2):
        arr1_pointer = 0
        arr2_pointer = 0
        merged_arr = list()
        while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
            if arr1[arr1_pointer] < arr2[arr2_pointer]:
                merged_arr.append(arr1[arr1_pointer])
                arr1_pointer += 1
            else:
                merged_arr.append(arr2[arr2_pointer])
                arr2_pointer += 1
        if arr1_pointer < len(arr1):
            merged_arr += arr1[arr1_pointer : len(arr1)]
        if arr2_pointer < len(arr2):
            merged_arr += arr2[arr2_pointer : len(arr2)]
        return merged_arr
    # Big O
    
    @staticmethod
    def quick(array):
        Algorithm.quick_actual(array, 0, len(array) - 1)
    
    @staticmethod
    def quick_actual(array, left, right):
        sub_slice = right - left + 1
        if sub_slice < 2:
            return
        pivot_idx = right
        left_total = 0
        right_total = 1
        going_right = True
        for _ in range(sub_slice):
            if going_right:
                if array[left + left_total] >= array[pivot_idx]:
                    going_right = False
                    Algorithm.swap(array, left + left_total, pivot_idx)
                    pivot_idx = left + left_total
                left_total += 1
            else:
                if array[right - right_total] < array[pivot_idx]:
                    going_right = True
                    Algorithm.swap(array, right - right_total, pivot_idx)
                    pivot_idx = right - right_total
                right_total += 1
        Algorithm.quick_actual(array, left, pivot_idx - 1)
        Algorithm.quick_actual(array, pivot_idx + 1, right)
    
    @staticmethod
    def swap(array: list, idx1, idx2):
        array[idx1], array[idx2] = array[idx2], array[idx1]

def dont():
    total_quick = list()
    total_merge = list()
    for _ in range(10):
        start = datetime.datetime.now()
        arr = np.random.randint(10000000, size=(np.random.randint(1000000, 2000000)))
        # print(arr)
        arr = arr.tolist()
        print()
        # print(Algorithm.merge(arr))
        Algorithm.quick(arr)
        end = datetime.datetime.now()
        finish = end - start
        print(f"quick - {finish}")
        total_quick.append(finish)
        print()
        start = datetime.datetime.now()
        arr = np.random.randint(10000000, size=(np.random.randint(1000000, 2000000)))
        arr = arr.tolist()
        # print(Algorithm.merge(arr))
        arr = Algorithm.merge(arr)
        end = datetime.datetime.now()
        finish = end - start
        print(f"merge - {end - start}")
        total_merge.append(finish)
        print()
    total = datetime.datetime.now()
    total = total - total
    for time in total_quick:
        total += time
    print(f"total quick - {total}")
    total = datetime.datetime.now()
    total = total - total
    for time in total_merge:
        total += time
    print(f"total merge - {total}")

if __name__ == "__main__":
    dont()
    # array = np.random.randint(10000, size=(np.random.randint(100, 200)))
    # array = array.tolist()
    # Algorithm.quick(array)
    # print(array)