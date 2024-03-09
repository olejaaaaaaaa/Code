

import unittest

class Test(unittest.TestCase):
    def test(self):
        #only camelCase
        """
        
        error: solution(BreakPoint) == " Break Point"
                " Break Point" != "Break Point"

        ok: solution(nVertex) == "n Vertex"        

        """
        self.assertEqual(solution("breakPoint"), "break Point")
        self.assertEqual(solution("camelCaseStyle"), "camel Case Style")
        self.assertEqual(solution("jackSparrow"), "jack Sparrow")
        self.assertEqual(solution("laLaLa"), "la La La")

def solution(s):
    
    n: str = ""
    
    for i in s:
        if not i.isupper():
            n += i
        else:
            n += " " + i
    
    return n

if __name__ == "__main__":
    unittest.main()