from faker import Faker

fake = Faker()


class UsersProvider:
    @staticmethod
    def non_existent_user():
        return {
            "username": fake.name(),
            "password": fake.password(),
            "id": 12983874935636,
        }

    @staticmethod
    def existing_user():
        return {"username": "Olechka525", "id": 147033325}
