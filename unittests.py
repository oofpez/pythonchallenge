import unittest
import main


class SimpleTest(unittest.TestCase):

    # Returns true or false
    def test(self):
        self.assertTrue(True)

    def testSplitDraw(self):
        results = main.split_scores('test team A 0, test team B 0')
        self.assertEqual(1, (results[0].score))
        self.assertEqual(1, (results[1].score))

    def testSplitWinLose(self):
        results = main.split_scores('test team A 1, test team B 0')
        self.assertEqual(3, (results[0].score))
        self.assertEqual(0, (results[1].score))

    def testCreateOutput(self):
        results = main.create_output({'test Team A': main.teamScore('test Team A', 3), 'test Team B': main.teamScore('test Team B', 1)})
        self.assertEqual(['test Team A, 3 pts\n','test Team B, 1 pt\n'], (results))

if __name__ == '__main__':
    unittest.main()
