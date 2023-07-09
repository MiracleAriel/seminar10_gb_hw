# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "dog":
            return Dog(**kwargs)
        elif animal_type == "cat":
            return Cat(**kwargs)
        elif animal_type == "cow":
            return Cow(**kwargs)
        else:
            raise ValueError("Invalid animal type")

# Пример использования класса-фабрики
animal_type = "dog"
animal_params = {"name": "Buddy"}

animal = AnimalFactory.create_animal(animal_type, **animal_params)
print(animal.speak())  # Вывод: "Woof!"
print(animal.name)     # Вывод: "Buddy"
