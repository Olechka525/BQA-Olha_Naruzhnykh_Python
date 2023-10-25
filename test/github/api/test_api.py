from src.config.config import Config

def test_api():
    config = Config()
    print(config.request_timeout) 