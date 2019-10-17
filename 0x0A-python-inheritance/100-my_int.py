#!/usr/bin/python3
"""MyInt inherits from int"""


class MyInt(int):
    """MyInt inherits from int"""

    def __eq__(self, other):
        """change equal to not equal"""

        return super().__ne__(other)

    def __ne__(self, other):
        """change not equal to equal"""

        return super().__eq__(other)
