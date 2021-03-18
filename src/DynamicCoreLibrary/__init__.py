"""Main library."""

from robotlibcore import DynamicCore, keyword
from robot.api.deco import library
from DynamicCoreLibrary.mystuff import Library1, Library2
from robot.api import logger

@library
class DynamicCoreLibrary(DynamicCore):
    """
    General library documentation.
    
    This class will manage all registered keyword classes.
    """

    def __init__(self) -> None:
        libraries = [Library1(), Library2()]
        DynamicCore.__init__(self, libraries)

    @keyword
    def keyword_in_main(self) -> bool:
        """
        This keyword is in the main class.
        ----
        Examples:
        | Keyword in main |
        """
        logger.info(self.__class__)
        return True
