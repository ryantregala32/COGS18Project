import pandas as pd
import matplotlib.pyplot as plt
from my_module.functions import (
    column_analyzer,
    analyze_two_columns,
    compare_two_columns,
    create_line_plot,
    shot_distribution
)

def run_test(test_name,test_function, *arguments, assert_function = None):
    '''
    We are using a recursion function to make this test more readable
    with error handling

    Parameters:
    test_name : name of the test we are running
    test_function: the function we are calling to test
    *arguments: pass by reference that has the arguments to pass the test

    Returns:
    None because we are passing in a test
    '''
    try:
        # We are using f-string to pass in the name
        print(f"Running test: {test_name}...")
        # assinging resullt to call the arguments and the
        # test function
        result = test_function(*arguments)
        # We are using assert to check if the function
        # works
        if assert_function:
            assert_function(result)
        print(f"{test_name} passed.")
    except Exception as exc:
        # If the test fails, we are printing a statement
        print(f"{test_name} failed: {exc}")
    

def test_functions():
    # Create a sample DataFrame for testing
    data = {
        'Shots_Made': [10, 8, 15, 9, 5, 7, 20, 27],
        'Shots_Attempted': [15, 10, 20, 12, 7, 15, 25, 30],
        'Game': ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4', 'Quarter_5','Quarter_6', 'Quarter_7', 'Quarter_8' ],
         'Location_X': [0.2, 0.3, 0.4, 0.5, 0.7, 0.6, 0.8, 0.1],
    'Location_Y': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    }
    df = pd.DataFrame(data)
    # We are using a list
    # with a dictionary to make the code more readable and understandable
    test_run = [
        {
            "name" : "column_analyzer",
            "test_function" : column_analyzer,
            "arguments" : (df, 'Shots_Made'),
            "assert_function" : lambda res: isinstance(res, dict)
        },
        {
             "name" : "analyze_two_columns",
            "test_function" : analyze_two_columns,
            "arguments" : (df, 'Shots_Made', 'Shots_Attempted'),
            "assert_function" : None
        },
        {
            "name" : "compare_two_columns",
            "test_function" : compare_two_columns,
            "arguments" : (df, 'Shots_Made', 'Shots_Attempted'),
            "assert_function" : None
        },
        {
            "name" : "create_line_plot",
            "test_function" : create_line_plot,
            "arguments" : (df, 'Shots_Made', 'Shots_Attempted'),
            "assert_function" : None
        },
        {
            "name" : "shot_distribution",
            "test_function" : shot_distribution,
            "arguments" : (df, 'Location_X', 'Location_Y', 'Shots_Made', 'bright', 0.7),
            "assert_function" : None
        }
    ]
    # This iterates through the list and the dictionary keys, and runs the test.
    for test in test_run:
        run_test(test['name'], test['test_function'], *test['arguments'], assert_function = test['assert_function'])

# Here, we are calling the function to make sure the test runs
test_functions()
