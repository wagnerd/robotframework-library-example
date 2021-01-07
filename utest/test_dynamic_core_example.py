"""
Unittests for coverage_example
"""

from DynamicCoreLibrary import DynamicCoreLibrary

def test_method_one() -> None:
    """
    Cover keyword_in_main
    """
    assert DynamicCoreLibrary().keyword_in_main()
