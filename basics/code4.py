
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

def main():
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)
    dog3 = Dog("Bella", 2)

    print(dog1.bark())
    print(dog1.get_info())

    print(dog2.bark())
    print(dog2.get_info())

    print(dog3.bark())
    print(dog3.get_info())

if __name__ == "__main__":
    main()
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

def main():
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)
    dog3 = Dog("Bella", 2)

    print(dog1.bark())
    print(dog1.get_info())

    print(dog2.bark())
    print(dog2.get_info())

    print(dog3.bark())
    print(dog3.get_info())

if __name__ == "__main__":
    main()

