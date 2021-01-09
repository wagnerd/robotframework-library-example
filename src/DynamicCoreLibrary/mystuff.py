"""Library components."""

from robotlibcore import keyword


class Library1():
    """Class documentation."""

    @keyword
    def example(self) -> bool:
        """Keyword documentation."""
        self.not_keyword()
        return True

    @keyword
    def another_example(self, arg1: str, arg2: str ='defaultArg') -> bool:
        """
        Keyword documentation text.
        ----
        :param arg1: \n
        :param arg2:
        ----
        Examples:
        | Another Example | arg1 | arg2 |
        """
        self.not_keyword()
        print(arg1)
        print(arg2)
        return True

    def not_keyword(self) -> bool:
        """Keyword documentation."""
        print(self.__class__)
        return True


class Library2():
    """Class documentation."""

    @keyword('Custom name')
    def this_name_is_not_used(self) -> bool:
        """Keyword documentation."""
        self.not_keyword()
        return True

    @keyword(tags=['tag', 'another'])
    def tags(self) -> bool:
        """Keyword documentation."""
        self.not_keyword()
        return True

    def not_keyword(self) -> bool:
        """Keyword documentation."""
        print(self.__class__)
        return True
