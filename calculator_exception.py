class InvalidChar(Exception):
    """
    Raised when there is char that not ok
    good char:
    - digit
    - ()
    - + - * / ^ ! % ~
    """
    pass


class NumAfterNum(Exception):
    """
    Raised when there is number after number with space
    like:
    8+2+3 4*5/67
    """
    pass


class ExpressionOrder(Exception):
    """
    Raised when there is problem with the expression like:
    5+*8
    6/*2
    7(*9+2)
    """
    pass
