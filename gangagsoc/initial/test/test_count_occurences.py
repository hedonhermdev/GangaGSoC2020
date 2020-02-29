import sys, os
import unittest

parent_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')
sys.path.append(parent_path)

from count_occurences import extract_text, num_occurences

class TestCountOccurences(unittest.TestCase):
    def test_one(self):
        string = "There is the weather forecast for the day."
        num = num_occurences('the', string)
        self.assertEqual(num, 2)

    def test_two(self):
        string = "The; the, the! the the"
        num = num_occurences('the', string)
        self.assertEqual(num, 5)

