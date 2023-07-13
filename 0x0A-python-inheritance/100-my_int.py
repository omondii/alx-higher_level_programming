#!/usr/bin/python3
"""
No module imported
"""


class MyInt(int):
    """
    A class that inherits from int and overrides the == and != operators.
    """
    def __eq__(self, other):
        """
        Override the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator.
        """
        return super().__eq__(other)
