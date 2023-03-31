import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    # Test we get the right result string for a final score dictionary representing -
    def setUp(self):
        self.final_score = [
            {    
                "Home score": 3,
                "Away score": 1,
            },
            {    
                "Home score": 1,
                "Away score": 3,
            },
            {    
                "Home score": 3,
                "Away score": 3,
            },
        ]
    # Home win
    def test_can_get_a_home_win(self):
        expected_value = "Home win"
        actual_value = get_result(self.final_score[0])
        self.assertEqual(expected_value, actual_value)

    # Away win
    def test_can_get_an_away_win(self):
        expected_value = "Away win"
        actual_value = get_result(self.final_score[1])
        self.assertEqual(expected_value, actual_value)


    # Draw
    def test_can_get_a_draw_win(self):
        expected_value = "Draw"
        actual_value = get_result(self.final_score[2])
        self.assertEqual(expected_value, actual_value)

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_can_get_list_of_results(self):
        expected_value = ["Home win", "Away win", "Draw"]
        actual_value = get_results[self.final_scores]
        self.assertEqual(expected_value, actual_value)        




if __name__ == "__main__":
    unittest.main()
