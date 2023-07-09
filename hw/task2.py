# Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

import json

class DataSerializer:
    def __init__(self, data):
        self.data = data

    def serialize_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def deserialize_from_json(self, filename):
        with open(filename, 'r') as file:
            self.data = json.load(file)

# Пример использования методов класса DataSerializer
data = {'name': 'John', 'age': 30, 'city': 'New York'}

serializer = DataSerializer(data)

# Сериализация данных в JSON файл
serializer.serialize_to_json('data.json')

# Десериализация данных из JSON файла
serializer.deserialize_from_json('data.json')

# Вывод десериализованных данных
print(serializer.data)
