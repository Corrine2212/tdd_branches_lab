import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests

    # Test latest score (the last thing in the list)
    def test_can_get_latest_score(self):
        scores = [2, 4, 10, 2, 5]
        expected_value = 5
        actual_value = latest(scores)
        self.assertEqual(expected_value, actual_value)

    # Test personal best (the highest score in the list)
    
    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
