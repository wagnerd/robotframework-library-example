"""Main library."""

from robotlibcore import DynamicCore, keyword

from .mystuff import Library1, Library2


class DynamicCoreLibrary(DynamicCore):
    """General library documentation."""

    def __init__(self) -> None:
        libraries = [Library1(), Library2()]
        DynamicCore.__init__(self, libraries)

    @keyword
    def keyword_in_main(self) -> bool:
        """
        This keyword is in the main class.

        Examples:

        | Keyword in main |
        """
        print(self.__class__)
        return True
