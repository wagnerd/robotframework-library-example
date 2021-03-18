"""Library components."""

from robotlibcore import keyword
from robot.api import logger

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
        logger.info(arg1)
        logger.info(arg2)
        logger.debug("This will be debug")
        return True

    def not_keyword(self) -> bool:
        """Keyword documentation."""
        logger.info(self.__class__)
        logger.debug("This will be debug2")
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
        logger.info(self.__class__)
        return True
