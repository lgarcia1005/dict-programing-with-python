def greeting(name):
    print("Hello " + name + " How are you!")


def diff(x, y):
    return x - y


class User:
    def __init__(self, name, age, country):
        self.country = country
        self.age = age
        self.name = name

    def hello(self):
        print("Hello", self.name)
        print("Your Age:", self.age)
        print("Your Country:", self.country)

    def sum(self, x, y):
        return x + y
