import unittest
from isomorphs import Isomorph as iso

class IsomorphTests(unittest.TestCase):
    def test_make_string_map(self):
        expected = {
            "h" : 0,
            "e" : 1
        }
        actual = iso.make_string_map("he")
        
        self.assertEqual(expected, actual)
    
    def test_count_string_map(self):
        expected = {
            "h" : 1,
            "e" : 2
        }
        
        actual = iso.count_string_map("hee")
        
        self.assertEqual(expected, actual)
    
    def test_loose_isomorph_pattern(self):
        expected = (1, 1, 2)
        
        actual = iso.loose_isomorph_pattern("baby")
        
        self.assertEqual(expected, actual)
    
    def test_exact_isomorph_pattern(self):
        expected = (0, 1, 0, 2)
        
        actual = iso.exact_isomorph_pattern("baby")
        
        self.assertEqual(expected, actual)

    def test_all_group_isomorph_keys(self):
        expected = {
            "exact" : {
                (0, 1, 2) : ["bid", "rib"]
            },
            "loose" : {
                (1, 1, 1) : ["bid", "rib"]
            },
            "non_exact" : ["yay"],
            "non_loose" : ["yay"]
        }
        
        actual = iso.group_isomorphs(["bid", "rib", "yay"])
        
        self.assertEqual(expected["exact"], actual["exact"])
        self.assertEqual(expected["loose"], actual["loose"])
        self.assertEqual(expected["non_exact"], actual["non_exact"])
        self.assertEqual(expected["non_loose"], actual["non_loose"])
    
    def test_all_functions_raise_TypeError_with_null_input(self):
        with self.assertRaises(TypeError):
            iso.group_isomorphs(None)
        
        with self.assertRaises(TypeError):
            iso.exact_isomorph_pattern(None)
        
        with self.assertRaises(TypeError):
            iso.loose_isomorph_pattern(None)
        
        with self.assertRaises(TypeError):
            iso.count_string_map(None)
        
        with self.assertRaises(TypeError):
            iso.make_string_map(None)
    
    def test_group_raises_TypeError_with_null_elements(self):
        with self.assertRaises(TypeError):
            iso.group_isomorphs(["hello", None])
    
    def test_group_raises_TypeError_with_numeric_elements(self):
        with self.assertRaises(TypeError):
            iso.group_isomorphs([123, 456])

if __name__ == "__main__":
    unittest.main()