from faker import Faker

faker = Faker(locale="FR_fr")
class Addresses:

    @staticmethod
    def adresses_form():
        return {
            "address": faker.address(),
            "city": faker.city(),
            "state": "Tennessee",
            "cp": "22424",
            "homePhone": faker.phone_number(),
            "mobilePhone": faker.phone_number()
        }
