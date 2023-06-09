# parant class
class Mammal:

    legs = 4
    feeds_milk = True
    has_fur = True

# child class inheriting parent class


class Dog(Mammal):
    bark = True
    can_domesticate = True


# create an instance/object for dog class
Bulldog = Dog()

# print(Bulldog.bark)
print(Bulldog.feeds_milk)
print(issubclass(Dog, Mammal))
