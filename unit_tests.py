import unittest
from algorithms import Algorithm as algo
from isomorphs import Isomorph as iso

class SwapTests(unittest.TestCase):
    def test_swap(self):
        expected = [1, 2, 3]
        arr_to_swap = [2, 1, 3]
        
        algo.swap(arr_to_swap, 0, 1)
        
        self.assertEqual(expected, arr_to_swap)
    
    def test_swap_raises_IndexError(self):
        array = ["One thing is in this array, but really this is a 2d array because I'm a string"]
        with self.assertRaises(IndexError):
            algo.swap(array, 0, 1)

class BinarySearch(unittest.TestCase):
    def test_find_index(self):
        sorted_array = [0,1,2,3,4,5,6]
        expected_idx = 3
        
        self.assertEqual(sorted_array[expected_idx], sorted_array[algo.binary_search(expected_idx, sorted_array)])

    def test_element_not_in_array_raises_RecursionError(self):
        sorted_array = [0,1,2,4,5,6]
        element_to_find = 3
        with self.assertRaises(RecursionError):
            algo.binary_search(element_to_find, sorted_array)

    def test_single_element_array_index_found(self):
        sorted_array = [1]
        element_to_find = 1
        expected = 0
        
        self.assertEqual(expected, algo.binary_search(element_to_find, sorted_array))

    def test_sorted_array_is_null_raises_TypeError(self):
        with self.assertRaises(TypeError):
            algo.binary_search(0, None)

    def test_sorted_array_has_null_elements_raises_TypeError(self):
        with self.assertRaises(TypeError):
            algo.binary_search(0, [None, 1, None, 2, None, 3])

    def test_sorted_array_has_mixed_types_raises_TypeError(self):
        with self.assertRaises(TypeError):
            algo.binary_search(0, [0, "1", 2, "3", 4, "5"])

    def test_guess_all_returns(self):
        expected = 0
        correct = 2
        guess = 2
        self.assertEqual(expected, algo.guess(correct, guess))
        
        expected = 1
        correct = 2
        guess = 3
        self.assertEqual(expected, algo.guess(correct, guess))
        
        expected = -1
        correct = 2
        guess = 1
        self.assertEqual(expected, algo.guess(correct, guess))

class SortTests(unittest.TestCase):
    def test_sort_happy_path_integers(self):
        expected = [1, 2, 3, 4, 5, 6]
        arr_to_sort = [6, 5, 4, 3, 2, 1]
        
        actual = algo.bubble(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.insertion(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.selection(arr_to_sort.copy())
        self.assertEqual(actual, expected)
    
    def test_sort_happy_path_floats(self):
        expected = [.1, .2, .3, .4, .5, .6]
        arr_to_sort = [.6, .5, .4, .3, .2, .1]
        
        actual = algo.bubble(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.insertion(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.selection(arr_to_sort.copy())
        self.assertEqual(actual, expected)
    
    def test_sort_empty_array(self):
        expected = []
        arr_to_sort = []
        
        actual = algo.bubble(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.insertion(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.selection(arr_to_sort.copy())
        self.assertEqual(actual, expected)
    
    def test_sort_single_element_array(self):
        expected = [28734]
        arr_to_sort = [28734]
        
        actual = algo.bubble(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.insertion(arr_to_sort.copy())
        self.assertEqual(actual, expected)
        
        actual = algo.selection(arr_to_sort.copy())
        self.assertEqual(actual, expected)
    
    def test_sort_null_array_TypeError(self):
        with self.assertRaises(TypeError):
            algo.bubble(None)
        
        with self.assertRaises(TypeError):
            algo.insertion(None)
        
        with self.assertRaises(TypeError):
            algo.selection(None)
    
    def test_sort_mixed_types_TypeError(self):
        array = [1, "2", 3, "4"]
        
        with self.assertRaises(TypeError):
            algo.bubble(array.copy())
        
        with self.assertRaises(TypeError):
            algo.insertion(array.copy())
        
        with self.assertRaises(TypeError):
            algo.selection(array.copy())
    
    def test_sort_with_null_elements(self):
        array = [1, None, 3]
        
        with self.assertRaises(TypeError):
            algo.bubble(array.copy())
        
        with self.assertRaises(TypeError):
            algo.insertion(array.copy())
        
        with self.assertRaises(TypeError):
            algo.selection(array.copy())

if __name__ == "__main__":
    unittest.main()