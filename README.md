# BQA-Olha_Naruzhnykh_Python
This framework is designed in order to perform tests for github using  UI and API approaches.

## Framework structure
    src - source folder.
### Application module
This module contains applications for testing. GitHub folder was added.
This GitHub folder consists of 2 folder:
 -for api (with github_api class)
 -for ui (with github_ui class).

### Config module
This module contains configuration information and holds all the settings of framework.
Config classes are responsible to store framework's and env's configuration. Config variables are stored here.
Config module contains
 -'env' folder for saving variables in json format.
 -'Config_harder' class contains env's variables and uses json file source, registration, getter for the values.
 -'Config' class contains system variables, constants.

## Tests module
This module includes all tests. GitHub folder was added.
This GitHub folder consists of 2 folder:
 -for api test (with test_api class)
 -for ui test (with test_ui class).

