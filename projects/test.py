class Person:
    def __init__(self, name, birthYear, gender, address):
        self.name = name
        self.birthYear = birthYear
        self.gender = gender
        self.address = address

    # def __repr__(self):
    #     pass
        # return ("name: {}\n"
        #         "birthYear: {}\n"
        #         "gender: {}\n"
        #         "address: \n"
        #         "\tcountry: {}\n"
        #
        # "\ttown: {}".format(
        #             self.name, self.birthYear, self.gender,
        #             self.address.country, self.address.town))


iva = Person("Iva", 1977, "female", {
    "country": "Bulgaria", "town": "Sofia"})
pesho = Person("Pesho", 1975, "male", {
    "country": "Bulgaria", "town": "Plovdiv"})


def test(x):

    print("HI")


test(1)
