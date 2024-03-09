from typing import List
import unittest


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(disemvowel("This is for losers!"), "Ths s fr lsrs!")
        self.assertEqual(disemvowel("LOL"), "LL")



def disemvowel(string_: str):
    
    res: str = ""
    letters: List[str] = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

    for i in string_:

        b = False 
        for j in letters:
               
            if i == j:
                b = True

        if not b:
            res += i        

        
    return res

if __name__ == "__main__":
    unittest.main()