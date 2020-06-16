"""
Program name: function_parameter.py
Author: Rachel Li
Last date modified: 16 June 2020

The purpose of this program is to write a string printing message
"""
def multiply_string(n, message):
    """
    Use reST style.
    :param message: this is the string message
    :param n: number of times message printed
    :returns: message printed n times
    """
    # that takes a string message and a number n
    while True:
        try:
            for line in range(n):
                if n < 1 and n > 9:
                    print("n must be between 2 and 7")
                else:
                    break
        except ValueError:
            print("Input not valid")
            pass
        if 1 <= n <= 9:
            print("valid")
        else:
            print("input not valid")
        return str(n * message) # and returns the string with message printed n times.

if __name__ == '__main__':
    try:
        message = input("Enter word to print: ")
        n = int(input("Enter number of times to print: "))
    except ValueError:
        print("ValueError found")
    else:
        print(multiply_string(n, message))

#sample output
#'Python!Python!Python!Python!'
