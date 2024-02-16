#!/usr/bin/python3
"""Max Integer Function UnitTest
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):

    def test_list_has_different_value_datatypes(self):
        sample_list = ['5', [0, 1], 4, True]
        self.assertRaises(TypeError, max_integer, sample_list,
                          "TypeError raised")

    def test_list_has_all_integer_values(self):
        sample_list = [-10, 10, 2000, 50, 0, -2000]
        self.assertEqual(max_integer(sample_list), 2000,
                         "Function works for all integers")

    def test_list_has_positive_integer_values(self):
        sample_list = [100, 10, 2000, 50, 25]
        self.assertEqual(max_integer(sample_list),
                         2000, "Function works for positive integers")

    def test_list_has_negative_integer_values(self):
        sample_list = [-10, -15, -2000, -50, -2000]
        self.assertEqual(max_integer(sample_list),
                         -10, "Function works for negative integers")

    def test_list_has_duplicate_integer_values(self):
        sample_list = [0, 0, 0, 0, 0, 0]
        self.assertEqual(max_integer(sample_list),
                         0, "Function works for duplicate integers")

    def test_list_is_empty(self):
        sample_list = []
        self.assertIsNone(max_integer(sample_list),
                          "Function works for empty list")
    
    def test_list_has_single_value(self):
        sample_list = [1]
        self.assertEqual(max_integer(sample_list), 1,
                          "Function works for single value list")
        
    def test_list_has_asc_ord_value(self):
        sample_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(sample_list), 6,
                          "Function works for asc ord value list")
