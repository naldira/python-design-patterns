

"""
an intelligence agency doing background checks on people.
"""


class BackgroundCheck:
    """
    background check done via a third party.
    """
    def __init__(self, level: int, sanctioned: bool) -> None:
        """
        initialize the instance.
        Parameters
        ----------
        level: int:
            terrorism threat level.
        sanctioned: bool:
            whether the person is in sanctioned list.
        """
        self.level = level
        self.sanctioned = sanctioned

    def __call__(self) -> bool:
        """
        returns True if conditions are met (passed the background check).
        or returns False if conditions are not met
        (failed the background check).
        """
        if not self.sanctioned and self.level < 3:
            result = True
        else:
            result = False
        return result

    def __str__(self) -> str:
        """
        print whether background check was clear or not.
        """
        if self.__call__():
            result = 'background check: clear'
        else:
            result = 'background check: NOT CLEARED'
        return result


if __name__ == '__main__':
    ok = BackgroundCheck(0, False)
    print(ok())
    print(ok)
    notok = BackgroundCheck(4, False)
    print(notok())
    print(notok)
    notok_1 = BackgroundCheck(0, True)
    print(notok_1)
