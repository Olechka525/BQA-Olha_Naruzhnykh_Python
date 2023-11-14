from src.config.config_harder import JSONConfigProvider

from faker import Faker

fake = Faker()


class UsersProvider:
    @staticmethod
    def non_existent_user():
        return {
            "username": fake.name(),
            "password": fake.password(),
            "id": fake.unique.random_int(),
        }

    @staticmethod
    def existing_user():
        return {
            "username": JSONConfigProvider.get_user_data("USERNAME"),
            "id": JSONConfigProvider.get_user_data("ID"),
        }
