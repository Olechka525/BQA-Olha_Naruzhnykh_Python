import os


class Config:
    """Config class is responsible to store fremework's and env's configuration
    The following config variables are declared:
     - timeout for request
     - username
     - environment
     - domain"""

    domain_api = os.environ.get("GITHUB_DOMAIN_API", "https://api.github.com")
    domain_ui = os.environ.get("GITHUB_DOMAIN_UI", "https://github.com")

    request_timeout = 25
    user_name = os.environ.get("USERNAME")
    env = os.environ.get("BQA_ENV")


config = Config()

print(config.request_timeout)
print(config.user_name)
print(config.env)
