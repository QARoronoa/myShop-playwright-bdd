import random

from faker import Faker

faker = Faker(locale="fr_FR")

class Login:

    @staticmethod
    def createAccountEmail():
        return {
            "email": faker.email()
        }

    @staticmethod
    def form_information():
        return {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "pwd": faker.password(),
            "day": str(random.randint(1,28)),
            "month": str(random.randint(1,13)),
            "years": faker.year()
        }