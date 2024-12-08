import math

class Sphere:
    def __init__(self, radius):
        self.__radius = radius  # Закрытый атрибут для радиуса
    
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.__radius = value

    @property
    def volume(self):
        return (4 / 3) * math.pi * self.__radius**3  # Вычисляемый объем шара

    @staticmethod
    def about():
        print("Программа для расчета объема шара. Автор: Поярков А.Т., Саитгареев Д.И., Басимова Л.Р.")

# Пример использования
if __name__ == "__main__":
    Sphere.about()
    try:
        r = float(input("Введите радиус шара: "))
        sphere = Sphere(r)
        print(f"Объем шара с радиусом {sphere.radius}: {sphere.volume:.2f}")
    except ValueError as e:
        print(e)
