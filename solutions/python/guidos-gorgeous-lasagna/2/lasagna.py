"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPERATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preperation time in minutes
    
    :param number_of_layers: int - how many layers the lasagne should have
    :return: int - how much preperation time is needed for the given amount of layers in minutes
    """

    return number_of_layers * PREPERATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate how long one has been in the kitchen

    :param number_of_layers: int - how many layers the lasagne should have
    :param elapsed_bake_time: int - how long the lasagne has already been baked
    :return: int - the total time spend in the kitchen
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time