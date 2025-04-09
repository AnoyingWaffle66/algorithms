import unittest
from algorithms import Algorithm as algo

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