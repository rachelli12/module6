"""
Program name: validate_input_in_functions.py
Author: Rachel Li
Last date modified: 06/16/2020

The purpose of this program is to write a function
takes test_name, test_score and invalid_message
that validates test_score
ask user for valid test score until in range
and prints valid input as "test name: ##"
"""
#test_name is mandatory
#test_score is optional, default value
def score_input(test_name, test_score=0, invalid_message='Please try again'):
    """
    Use reST style.
    :param test_name: this represents test name
    :param test_score: this represents test score
    :param invalid_message: this represents message if input invalid
    :returns: test_name: test_score
    :raises keyError: raises an exception
    """
    #return {test_name: test_score}
    try:
        test = test_name
        score = int(test_score)
        if 0 <= score <= 100:
            return f'{test}: {score}'
        else:
            return "Please try again"
    except ValueError as err:
        print("ValueError occurred", err)
        raise ValueError

if __name__ == '__main__':
    try:
        test_name = input("Enter test name: ")
        test_score = int(input("Enter test score: "))
        invalid_message = "Please try again"
    except ValueError as err:
        print("ValueError occurred")
    else:
        print(score_input(test_name, test_score, invalid_message))

