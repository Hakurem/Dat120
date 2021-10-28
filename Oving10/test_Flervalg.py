#Øving10

#a) Enhets_test for flervalg


import unittest
from FlervalgScript import Flervalg #import a class




class test_Flervalg(unittest.TestCase): #inheritance

    def getValues(self):
        question = "1+1 is?"
        answers = ["1","2","3"]
        correct = "1" #index 1 is correct answer (2)
        Instance = Flervalg(question,answers,correct)
        return question,answers,correct,Instance

    def test_getanswer(self):
        question,answers,correct,Instance = self.getValues()
        expected = "2"
        got = Instance.getanswer()
        self.assertEqual(got,expected)

    def test_checkans(self):
        question,answers,correct,Instance = self.getValues()
        my_answer = "0"
        result = Instance.checkans(my_answer)
        expected = False
        got = my_answer == result
        self.assertFalse(got,expected)


    

if __name__ == "__main__":
    unittest.main()
