# Final

> Programming Design 2023

## 01. Define a function `factorial()` which returns the result of $n!$.

Source: <https://en.wikipedia.org/wiki/Factorial>

```python
def factorial(n: int) -> int:
    """
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `symbolic_reduce()` which reduces given `list` based on a symbolic operator.

```python
def symbolic_reduce(x: list, operator: str) -> int:
    """
    >>> symbolic_reduce([1, 2, 3, 4, 5], "+")
    15
    >>> symbolic_reduce([1, 2, 3, 4, 5], "-")
    -13
    >>> symbolic_reduce([1, 2, 3, 4, 5], "*")
    120
    >>> symbolic_reduce([1, 2, 3, 4, 5, 6, 7], "+")
    28
    >>> symbolic_reduce([1, 2, 3, 4, 5, 6, 7], "-")
    -26
    >>> symbolic_reduce([1, 2, 3, 4, 5, 6, 7], "*")
    5040
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a class `ListMethods()` which instantiates objects with three methods `sort_asc()`, `sort_desc()` and `reverse()`.

```python
class ListMethods:
    """
    >>> list_methods = ListMethods([3, 2, 7, 5, 11])
    >>> type(list_methods)
    '__main__.ListMethods'
    >>> list_methods.sort_asc()
    [2, 3, 5, 7, 11]
    >>> list_methods.sort_desc()
    [11, 7, 5, 3, 2]
    >>> list_methods.reverse()
    [11, 5, 7, 2, 3]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a class `Fibonacci` which instantiates objects with two methods `get_nth_int()` and `get_sequence()`.

Source: <https://en.wikipedia.org/wiki/Fibonacci_sequence>

```python
class Fibonacci:
    """
    >>> fibonacci = Fibonacci(5)
    >>> type(sort_args)
    '__main__.Fibonacci'
    >>> fibonacci.get_nth_int(1)
    0
    >>> fibonacci.get_nth_int(2)
    1
    >>> fibonacci.get_nth_int(3)
    1
    >>> fibonacci.get_nth_int(4)
    2
    >>> fibonacci.get_nth_int(5)
    3
    >>> fibonacci.get_sequence()
    [0, 1, 1, 2, 3]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a class `Prime` which instantiates objects with 2 methods `get_nth_int()` and `get_sequence()`.

Source: <https://en.wikipedia.org/wiki/Prime_number>

```python
class Prime:
    """
    >>> prime = Prime(5)
    >>> type(prime)
    '__main__.Prime'
    >>> prime.get_nth_int(1)
    2
    >>> prime.get_nth_int(2)
    3
    >>> prime.get_nth_int(3)
    5
    >>> prime.get_nth_int(4)
    7
    >>> prime.get_nth_int(5)
    11
    >>> prime.get_sequence()
    [2, 3, 5, 7, 11]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a class `Rot13` which instantiates objects with 2 methods `rotate_character()` and `rotate_sentence()`.

Source: <https://en.wikipedia.org/wiki/ROT13>

```python
class Rot13:
    """
    >>> rot13 = Rot13()
    >>> type(rot13)
    '__main__.Rot13'
    >>> rot13.rotate_character("A")
    'N'
    >>> rot13.rotate_character("B")
    'O'
    >>> rot13.rotate_character("L")
    'Y'
    >>> rot13.rotate_character("M")
    'Z'
    >>> rot13.rotate_character("a")
    'n'
    >>> rot13.rotate_character("b")
    'o'
    >>> rot13.rotate_character("l")
    'y'
    >>> rot13.rotate_character("m")
    'z'
    >>> rot13.rotate_sentence("Abj vf orggre guna arire.")
    'Now is better than never.'
    >>> rot13.rotate_sentence("Now is better than never.")
    'Abj vf orggre guna arire.'
    >>> rot13.rotate_sentence("Rkcyvpvg vf orggre guna vzcyvpvg.")
    'Explicit is better than implicit.'
    >>> rot13.rotate_sentence("Explicit is better than implicit.")
    'Rkcyvpvg vf orggre guna vzcyvpvg.'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `get_optimal_change()` in New Taiwan Dollar currency system. By saying "optimal" means the cashier has enough amount of all currency amounts in coins and notes, and the cashier strives for giving customer as few as possible.

```python
def get_optimal_change(sale_price: int, paid: int) -> dict:
    """
    >>> get_optimal_change(35, 50)
    {500: 0, 100: 0, 50: 0, 10: 1, 5: 1, 1: 0}
    >>> get_optimal_change(69, 100)
    {500: 0, 100: 0, 50: 0, 10: 3, 5: 0, 1: 1}
    >>> get_optimal_change(124, 150)
    {500: 0, 100: 0, 50: 0, 10: 2, 5: 1, 1: 1}
    >>> get_optimal_change(124, 200)
    {500: 0, 100: 0, 50: 1, 10: 2, 5: 1, 1: 1}
    >>> get_optimal_change(124, 500)
    {500: 0, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1}
    >>> get_optimal_change(124, 1000)
    {500: 1, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1}
    >>> get_optimal_change(1124, 1500)
    {500: 0, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1}
    >>> get_optimal_change(1124, 2000)
    {500: 1, 100: 3, 50: 1, 10: 2, 5: 1, 1: 1}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `import_teams_json()` which imports `mlb_teams.json` and `nba_teams.json` in working directory.

```python
def import_teams_json() -> tuple:
    """
    >>> mlb_teams, nba_teams = import_teams_json()
    >>> type(mlb_teams)
    list
    >>> type(nba_teams)
    dict
    >>> len(mlb_teams)
    30
    >>> len(nba_teams["data"])
    30
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `get_cities_locations()` which extracts the `locationName` and `city` from `mlb_teams.json` and `nba_teams.json` respectively in working directory.

```python
def get_cities_locations() -> tuple:
    """
    >>> mlb_locations, nba_cities = get_cities_locations()
    >>> len(mlb_locations)
    30
    >>> len(nba_cities)
    30
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `find_cities_locations_with_full_name()` which returns the locations or cities given team's full name from `mlb_teams.json` and `nba_teams.json` in working directory.

```python
def find_cities_locations_with_full_name(team_full_name: str) -> str:
    """
    >>> find_cities_locations_with_full_name("New York Yankees")
    'Bronx'
    >>> find_cities_locations_with_full_name("New York Mets")
    'Flushing'
    >>> find_cities_locations_with_full_name("Miami Heat")
    'Miami'
    >>> find_cities_locations_with_full_name("Denver Nuggets")
    'Denver'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```