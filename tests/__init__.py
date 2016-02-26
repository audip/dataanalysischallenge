import unittest

class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        """
        Check the test suite runs by affirming 2+2=4
        """
        self.assertEqual(2+2, 4)

    def test_objectCreateProblem1(self):
        """
        Checks for object creation for class in Problem 1
        """
        from problem1 import babyDetails
        testBaby = babyDetails()
        self.assertEqual(testBaby.testObjectCreation(), "Object creation successful")

    def test_objectCreateProblem2(self):
        """
        Checks for object creation for class in Problem 2
        """
        from problem2 import babyDetails
        testBaby = babyDetails()
        self.assertEqual(testBaby.testObjectCreation(), "Object creation successful")
