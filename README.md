# Robot Framework Library Example

This project is used as a simple example for a RobotFramework library and contains some mechanisms I learned and I want to keep for the future :)

Feel free to reuse this repository for your own library projects!

This README is copied into the library package, so it should contain some information about the package and the usage.

It is also used as the `long_description` in [setup.cfg](setup.cfg) for the package.

This project welcomes contributions and suggestions.

## Structure
The folder structure is based on the structure of several 
other RobotFramework libraries and even on RobotFramework itself.

The the source and structure is based on the example inside [PythonLibCore](https://github.com/robotframework/PythonLibCore).

## Logging

Logging in keywords should be done using the `robot.api.logger`.

During debugging and development, robot tests should be run using `--loglevel DEBUG` or `--loglevel DEBUG:INFO` which will limit the loglevel inside the report to INFO.