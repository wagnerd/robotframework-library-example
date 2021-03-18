*** Settings ***
Documentation    Acceptance tests for the library package
Library        ${LIBRARY}

*** Variables ***
${LIBRARY}    DynamicCoreLibrary


*** Test Cases ***
Keyword names
    [Documentation]    Checking some library keywords exist
    Log    ${LIBRARY}
    Keyword in main
    Example
    Another Example    arg1
    Custom name
