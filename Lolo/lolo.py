
import unittest

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(f("how do"), "How Do")
        self.assertEqual(f("hOw dO"), "How Do")
        self.assertEqual(f("hoW DO yOu dO?"), "How Do You Do?")


def f(s: str) -> str:
    
    result: str = ""

    for i in s.split():

        isFirst: bool = True
        
        for n in i:

            if isFirst:
                if n.islower():
                    n = n.upper()
            else:
                if n.isupper():
                    n = n.lower()  

            isFirst = False          
            result += n

        result += " "    


    result = result[:-1]

    return result      
            

if __name__ == "__main__":
    unittest.main()







