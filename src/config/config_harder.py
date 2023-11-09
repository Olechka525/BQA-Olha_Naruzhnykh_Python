import json
import os
from typing import Any


class OSConfigProvider:
    @staticmethod
    def get(item_name: str) -> Any:
        value = os.getenv(item_name)  # get value from system envs
        return value  # return the value


class JSONConfigProvider:
    @staticmethod
    def _read_config(config_path):  # parse json file
        with open(config_path) as json_file:  # open json file
            return json.load(json_file)  # convert to dict/treeMap

    @staticmethod
    def get(item_name: str) -> Any:
        value = JSONConfigProvider._read_config(
            ".\src\config\envs\qa.json"
        )  # Read the file
        return value.get(item_name)  # get the value from the file by parameter name


class Config:
    """
    Holds all the settings of your framework
    """

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers  # STORE THE ORDER OF PROVIDERS/SOURCES

        self.conf_dict = {}  # STORE OF VALUES OF PARAMETERS

        # BLOCK FOR REGISTERING THE PARAMETERS
        self._register("PARAMETER_JSON")
        self._register("PARAMETER_ENV")

    def __getattr__(self, item_name: str) -> Any:
        if item_name not in self.conf_dict:  # if no value - raise an error
            raise AttributeError(f"Please register '{item_name}' var before usage")

        return self.conf_dict[item_name]  # else - return value

    def _register(self, item_name: str) -> None:
        """
        Retrieves the value of parameter with item_name name from the
        config providers/sources and store it in config class for later usage
        """
        for (
            provider
        ) in self.config_providers:  # iterate over list of config providers/sources
            value = provider.get(
                item_name
            )  # try to get value by name from config providers/sources
            if value is not None:  # if value exists/retrived
                self.conf_dict[item_name] = value  # save it to config class
                return  # STOP further search

        raise ValueError(
            f"{item_name} name is missing in config providers"
        )  # if no value for parameter item_name name found - stop TEST FRAMEWOEK execution


config = Config([OSConfigProvider, JSONConfigProvider])

print(config.get("PARAMETER_JSON"))
print(config.get("PARAMETER_ENV"))
