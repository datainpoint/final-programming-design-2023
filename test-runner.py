import unittest
import importlib

class TestFinal(unittest.TestCase):
    def test_01_factorial(self):
        self.assertEqual(asgmt.factorial(0), 1)
        self.assertEqual(asgmt.factorial(1), 1)
        self.assertEqual(asgmt.factorial(2), 2)
        self.assertEqual(asgmt.factorial(3), 6)
        self.assertEqual(asgmt.factorial(4), 24)
        self.assertEqual(asgmt.factorial(5), 120)
        self.assertEqual(asgmt.factorial(6), 720)
    def test_02_symbolic_reduce(self):
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3, 4, 5], "+"), 15)
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3, 4, 5], "-"), -13)
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3, 4, 5], "*"), 120)
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3, 4, 5, 6, 7], "+"), 28)
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3, 4, 5, 6, 7], "-"), -26)
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3, 4, 5, 6, 7], "*"), 5040)
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3], "+"), 6)
        self.assertEqual(asgmt.symbolic_reduce([1, 2, 3], "*"), 6)
    def test_03_ListMethods(self):
        list_methods = asgmt.ListMethods([3, 2, 7, 5, 11])
        self.assertEqual(list_methods.sort_asc(), [2, 3, 5, 7, 11])
        self.assertEqual(list_methods.sort_desc(), [11, 7, 5, 3, 2])
        self.assertEqual(list_methods.reverse(), [11, 5, 7, 2, 3])
        list_methods = asgmt.ListMethods([1, 2, 3])
        self.assertEqual(list_methods.sort_asc(), [1, 2, 3])
        self.assertEqual(list_methods.sort_desc(), [3, 2, 1])
        self.assertEqual(list_methods.reverse(), [3, 2, 1])
    def test_04_Fibonacci(self):
        fibonacci = asgmt.Fibonacci(5)
        self.assertEqual(fibonacci.get_nth_int(1), 0)
        self.assertEqual(fibonacci.get_nth_int(2), 1)
        self.assertEqual(fibonacci.get_nth_int(3), 1)
        self.assertEqual(fibonacci.get_nth_int(4), 2)
        self.assertEqual(fibonacci.get_nth_int(5), 3)
        self.assertEqual(fibonacci.get_sequence(), [0, 1, 1, 2, 3])
        fibonacci = asgmt.Fibonacci(10)
        self.assertEqual(fibonacci.get_nth_int(6), 5)
        self.assertEqual(fibonacci.get_nth_int(7), 8)
        self.assertEqual(fibonacci.get_nth_int(8), 13)
        self.assertEqual(fibonacci.get_nth_int(9), 21)
        self.assertEqual(fibonacci.get_nth_int(10), 34)
        self.assertEqual(fibonacci.get_sequence(), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    def test_05_Prime(self):
        prime = asgmt.Prime(5)
        self.assertEqual(prime.get_nth_int(1), 2)
        self.assertEqual(prime.get_nth_int(2), 3)
        self.assertEqual(prime.get_nth_int(3), 5)
        self.assertEqual(prime.get_nth_int(4), 7)
        self.assertEqual(prime.get_nth_int(5), 11)
        self.assertEqual(prime.get_sequence(), [2, 3, 5, 7, 11])
        prime = asgmt.Prime(10)
        self.assertEqual(prime.get_nth_int(6), 13)
        self.assertEqual(prime.get_nth_int(7), 17)
        self.assertEqual(prime.get_nth_int(8), 19)
        self.assertEqual(prime.get_nth_int(9), 23)
        self.assertEqual(prime.get_nth_int(10), 29)
        self.assertEqual(prime.get_sequence(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    def test_06_Rot13(self):
        rot13 = asgmt.Rot13()
        self.assertEqual(rot13.rotate_character("A"), 'N')
        self.assertEqual(rot13.rotate_character("B"), 'O')
        self.assertEqual(rot13.rotate_character("L"), 'Y')
        self.assertEqual(rot13.rotate_character("M"), 'Z')
        self.assertEqual(rot13.rotate_character("a"), 'n')
        self.assertEqual(rot13.rotate_character("b"), 'o')
        self.assertEqual(rot13.rotate_character("l"), 'y')
        self.assertEqual(rot13.rotate_character("m"), 'z')
        self.assertEqual(rot13.rotate_sentence("Abj vf orggre guna arire."),
                         "Now is better than never.")
        self.assertEqual(rot13.rotate_sentence("Now is better than never."),
                         "Abj vf orggre guna arire.")
        self.assertEqual(rot13.rotate_sentence("Rkcyvpvg vf orggre guna vzcyvpvg."),
                         "Explicit is better than implicit.")
        self.assertEqual(rot13.rotate_sentence("Explicit is better than implicit."),
                         "Rkcyvpvg vf orggre guna vzcyvpvg.")
    def test_07_get_optimal_change(self):
        self.assertEqual(asgmt.get_optimal_change(18, 20),
                         {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 2})
        self.assertEqual(asgmt.get_optimal_change(18, 50),
                         {500: 0, 100: 0, 50: 0, 10: 3, 5: 0, 1: 2})
        self.assertEqual(asgmt.get_optimal_change(18, 100),
                         {500: 0, 100: 0, 50: 1, 10: 3, 5: 0, 1: 2})
        self.assertEqual(asgmt.get_optimal_change(18, 500),
                         {500: 0, 100: 4, 50: 1, 10: 3, 5: 0, 1: 2})
        self.assertEqual(asgmt.get_optimal_change(18, 1000),
                         {500: 1, 100: 4, 50: 1, 10: 3, 5: 0, 1: 2})
        self.assertEqual(asgmt.get_optimal_change(35, 50),
                         {500: 0, 100: 0, 50: 0, 10: 1, 5: 1, 1: 0})
        self.assertEqual(asgmt.get_optimal_change(69, 100),
                         {500: 0, 100: 0, 50: 0, 10: 3, 5: 0, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(104, 105),
                         {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(104, 110),
                         {500: 0, 100: 0, 50: 0, 10: 0, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(104, 150),
                         {500: 0, 100: 0, 50: 0, 10: 4, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(104, 200),
                         {500: 0, 100: 0, 50: 1, 10: 4, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(104, 500),
                         {500: 0, 100: 3, 50: 1, 10: 4, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(104, 1000),
                         {500: 1, 100: 3, 50: 1, 10: 4, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(124, 150),
                         {500: 0, 100: 0, 50: 0, 10: 2, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(124, 200),
                         {500: 0, 100: 0, 50: 1, 10: 2, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(124, 500),
                         {500: 0, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(124, 1000),
                         {500: 1, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(1124, 1500),
                         {500: 0, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1})
        self.assertEqual(asgmt.get_optimal_change(1124, 2000),
                         {500: 1, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1})
    def test_08_import_teams_json(self):
        mlb_teams, nba_teams = asgmt.import_teams_json()
        self.assertIsInstance(mlb_teams, list)
        self.assertIsInstance(nba_teams, dict)
        self.assertEqual(len(mlb_teams), 30)
        self.assertEqual(len(nba_teams["data"]), 30)
    def test_09_get_cities_locations(self):
        mlb_locations, nba_cities = asgmt.get_cities_locations()
        self.assertEqual(len(mlb_locations), 30)
        self.assertEqual(len(nba_cities), 30)
        self.assertIn("Bronx", mlb_locations)
        self.assertIn("Flushing", mlb_locations)
        self.assertIn("Denver", nba_cities)
        self.assertIn("Miami", nba_cities)
        self.assertIn("Boston", nba_cities)
        self.assertIn("Los Angeles", nba_cities)
    def test_10_find_cities_locations_with_full_name(self):
        self.assertEqual(asgmt.find_cities_locations_with_full_name("New York Yankees"), 'Bronx')
        self.assertEqual(asgmt.find_cities_locations_with_full_name("New York Mets"), 'Flushing')
        self.assertEqual(asgmt.find_cities_locations_with_full_name("Miami Heat"), 'Miami')
        self.assertEqual(asgmt.find_cities_locations_with_full_name("Denver Nuggets"), 'Denver')
        self.assertEqual(asgmt.find_cities_locations_with_full_name("Boston Celtics"), 'Boston')
        self.assertEqual(asgmt.find_cities_locations_with_full_name("Boston Red Sox"), 'Boston')
        
asgmt = importlib.import_module("final")
suite = unittest.TestLoader().loadTestsFromTestCase(TestFinal)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))