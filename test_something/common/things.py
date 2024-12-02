"""
This is some module docstring.

I add another line of nonsense to fill this docstring.
Very important things should be stated in this part of the documentation.
"""

class ClassA:
  """
  Some class docstring for 'ClassA'.

  This is not the same as in '__init__()' function, hopefully.
  """
  
  def __init__(self):
    """
    Init docstring.
    """
    print("ClassA initialized.")


  def fun1(self, number: int = 0):
    """
    This function prints a number.

    :param number: An integer.
    """
    print(number)

  def square_number(self, number: int) -> int:
    """
    Returns the square of a number.

    This is a handy way to get the square of any number.
    
    :param number: Some integer.
    :return: Square of number.
    """
    return number * number


def module_function():
  """
  Says 'Hello' to you.
  """
  print("Hello!")
