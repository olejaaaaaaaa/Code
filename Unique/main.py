
from unittest import TestCase
import unittest

class Test(TestCase):

	def test(self):
		self.assertEqual(
            unique_in_order("AAABBBCCDERfRT"), 
            ["A", "B", "C", "D", "E", "R", "f", "R", "T"]
        )


def unique_in_order(sequence):
    
    if len(sequence) == 0:
        return []
    
    res = [sequence[0]]
    prev = sequence[0]
    
    for i in sequence:
        if i != prev:
            res.append(i)
            prev = i
        
    return res


if __name__ == "__main__":
     unittest.main()