"""The most over-engineered calculator."""
from functools import reduce


class CalculatorValueError(ValueError):
    """Custom ValueError for calculation operations."""

    pass


class CalculatorTypeError(TypeError):
    """Custom Type Error for calculation operations."""

    pass


def _convert_num(s):
    """Convert a numeric string to a number.

    Args:
        s (str): A number representing a string

    Returns:
        int or float: The numeric representation of the string

    """
    try:
        return int(s)
    except ValueError:
        return float(s)


def _check_input(inp, check_div_case=False, check_pow_case=False):
    """Validate the input for the aggregation functions.

    Args:
        inp (list): An list that is hopefully of numbers
        check_div_case (bool): Whether to assert checks for division.
        check_pow_case (bool): Whether to assert checks for power.

    Returns:
        inp: converted input data

    Raises:
        CalculatorTypeError: If the input is not a list or tuple.
        CalculatorValueError: If the input contains fewer than 2 items, if \
            any inputs are not numbers, or if any items after the first are \
            zero when diving.

    """
    if not isinstance(inp, (list, tuple)):
        raise CalculatorTypeError(f"Input must be a list, received: {inp}.")
    elif len(inp) < 2:
        raise CalculatorValueError(
            "Input list must have at least two items, received input of "
            f"length {len(inp)}."
        )
    elif not all(isinstance(n, (int, float)) for n in inp):
        try:
            inp = [_convert_num(n) for n in inp]
        except ValueError:
            raise CalculatorValueError(
                f"All inputs must be a number, received: {inp}."
            )

    if check_div_case and (0 in inp[1:]):
        raise CalculatorValueError(
            "No items after the first cannot be zero when diving."
        )

    if check_pow_case and ((0 == inp[0]) and (len(inp) == 2) and (inp[1] < 0)):
        raise CalculatorValueError("0 cannot be raised to a negative power.")

    return inp


def sum_(nums):
    """Find the sum of a list of numbers.

    Example:
        >>> sum_([1, 2, 3, 4])
        10

    Args:
        nums (list): A list of numbers

    Returns:
        int or float: The sum

    """
    return sum(_check_input(nums))


def difference(nums):
    """Find the difference of a list of numbers.

    Example:
        >>> difference([1, 2, 3, 4])
        -8

    Args:
        nums (list): A list of numbers

    Returns:
        int or float: The difference

    """
    return reduce(lambda n1, n2: n1 - n2, _check_input(nums))


def product(nums):
    """Find the product of a list of numbers.

    Example:
        >>> product([1, 2, 3, 4])
        24

    Args:
        nums (list): A list of numbers

    Returns:
        int or float: The product

    """
    return reduce(lambda n1, n2: n1 * n2, _check_input(nums))


def quotient(nums):
    """Find the quotient of a list of numbers.

    Example:
        >>> quotient([1, 2, 3, 4])
        0.041666666666666664

    Args:
        nums (list): A list of numbers

    Returns:
        int or float: The quotient

    """
    return reduce(
        lambda n1, n2: n1 / n2, _check_input(nums, check_div_case=True)
    )


def power(nums):
    """Find the power of a list of numbers.

    {1}^{2}^{3}

    Args:
        nums (list): A list of numbers

    Returns:
        int or float: The power

    """
    return reduce(
        lambda n1, n2: n1**n2, _check_input(nums, check_pow_case=True)
    )
