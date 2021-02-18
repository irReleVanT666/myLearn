import unittest

from class_14 import my_map, modify_multi

class TestMap(unittest.TestCase):

    def test_sum_function(self):
        self.assertEqual(my_map([1,3,5], modify_multi), [2,6,10])
        self.assertRaises(TypeError, my_map, (None, modify_multi))
        # self.assertNotEqual(my_sum([3,4,5]), 11)
        # self.assertNotEqual(my_sum([3, 4, 5]), 10)
        # self.assertRaises(TypeError, my_sum, None)
        self.assertNotEqual(my_map(('1', '3', '5'), modify_multi), ['11', '33', '55'])

if __name__ == '__main__' :
    unittest.main()




