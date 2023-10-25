import os

class Config:
    """ Config class is responsible to store fremework's and env's configuration 
    The following config variables are declared:
     - timeout for request
     - username
     - environment """
    
    request_timeout = 25
    user_name = os.environ.get('USERNAME')
    env = os.environ.get('BQA_ENV')

config = Config()

print(config.request_timeout)
print(config.user_name)
print(config.env)