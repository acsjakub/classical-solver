#!/usr/bin/python3

import unittest
import analyser

class TestStringAnalyser(unittest.TestCase):

    def test_count_frequency(self):
        sa = analyser.StringAnalyser()

        s1 = 'aaabbccc'
        s2 = 'abcbcacbacdcvcb'
        res1 = {'a': 37.5, 'b': 25, 'c': 37.5}
        res2 = {'a': 3/len(s2)*100, 'b': 4/len(s2)*100,
            'c': 6/len(s2)*100, 'd': 1/len(s2)*100, 'v': 1/len(s2)*100}

        self.assertEqual(sa.count_frequency(s1), res1)
        self.assertEqual(sa.count_frequency(s2), res2)

if __name__ == '__main__':
    unittest.main()
