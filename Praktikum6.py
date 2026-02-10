"""
==================================================
АВТОМОБИЛЬНАЯ КОНФИГУРАЦИОННАЯ СИСТЕМА
==================================================
Проект реализует объектно-ориентированную систему
моделирования автомобилей с использованием композиции.
Все компоненты: двигатель, кузов, колеса - являются
отдельными классами, объединяемыми в классе Car.
==================================================
"""


# ==================== ИМПОРТЫ ====================
# В данном проекте не используются библиотеки,
# все классы реализованы Python.
# =================================================


# ==================== КЛАССЫ =====================
# Каждый компонент автомобиля представлен отдельным классом
# с собственной логикой и методами отображения информации.
# =================================================


# ---------- КЛАСС ДВИГАТЕЛЯ ----------
# Отвечает за характеристики двигателя: мощность и тип топлива
# Используется в композиции с классом Car
class Engine:
    """Класс двигателя автомобиля"""

    def __init__(self, max_power, fuel_type):
        """
        Инициализация двигателя

        Параметры:
        - max_power: максимальная мощность в л.с. (int/float)
        - fuel_type: тип топлива (str)
        """
        self.max_power = max_power  # максимальная мощность в л.с.
        self.fuel_type = fuel_type  # тип топлива

    def display_info(self):
        """Возвращает строку с информацией о двигателе"""
        return f"Двигатель: {self.max_power} л.с., топливо: {self.fuel_type}"

    def __str__(self):
        """Строковое представление объекта (используется в print)"""
        return self.display_info()


# ---------- КЛАСС КУЗОВА ----------
# Отвечает за характеристики кузова: тип и количество дверей
# Используется в композиции с классом Car
class CarBody:
    """Класс кузова автомобиля"""

    def __init__(self, body_type, doors_count):
        """
        Инициализация кузова

        Параметры:
        - body_type: тип кузова (str)
        - doors_count: количество дверей (int)
        """
        self.body_type = body_type  # тип кузова
        self.doors_count = doors_count  # количество дверей

    def display_info(self):
        """Возвращает строку с информацией о кузове"""
        return f"Кузов: {self.body_type}, дверей: {self.doors_count}"

    def __str__(self):
        """Строковое представление объекта"""
        return self.display_info()


# ---------- КЛАСС КОЛЕСА ----------
# Отвечает за характеристики колеса: диаметр и тип резины
# Создается 4 экземпляра для каждого автомобиля
class Wheel:
    """Класс колеса автомобиля"""

    def __init__(self, diameter, tire_type):
        """
        Инициализация колеса

        Параметры:
        - diameter: диаметр в дюймах (int/float)
        - tire_type: тип резины (str)
        """
        self.diameter = diameter  # диаметр в дюймах
        self.tire_type = tire_type  # тип резины

    def display_info(self):
        """Возвращает строку с информацией о колесе"""
        return f"Колесо: {self.diameter}\", резина: {self.tire_type}"

    def __str__(self):
        """Строковое представление объекта"""
        return self.display_info()


# ---------- ОСНОВНОЙ КЛАСС АВТОМОБИЛЯ ----------
# Объединяет все компоненты в целый автомобиль
# Реализует бизнес-логику: расчет стоимости, запуск двигателя
class Car:
    """Основной класс автомобиля, объединяющий все компоненты"""

    def __init__(self, brand, model, year, engine, car_body, wheels):
        """
        Инициализация автомобиля

        Параметры:
        - brand: марка автомобиля (str)
        - model: модель автомобиля (str)
        - year: год выпуска (int)
        - engine: объект класса Engine
        - car_body: объект класса CarBody
        - wheels: список из 4 объектов класса Wheel

        Исключения:
        - ValueError: если передано не 4 колеса
        """
        # Валидация входных данных
        if len(wheels) != 4:
            raise ValueError("Автомобиль должен иметь 4 колеса!")

        # Основные характеристики автомобиля
        self.brand = brand
        self.model = model
        self.year = year

        # КОМПОЗИЦИЯ: автомобиль "имеет" следующие компоненты
        self.engine = engine  # композиция: автомобиль "имеет" двигатель
        self.car_body = car_body  # композиция: автомобиль "имеет" кузов
        self.wheels = wheels  # композиция: автомобиль "имеет" 4 колеса

    # ========== МЕТОДЫ ОТОБРАЖЕНИЯ ИНФОРМАЦИИ ==========
    # Раздельная информация о каждом компоненте
    def display_engine_info(self):
        """Выводит информацию только о двигателе"""
        print("=== Информация о двигателе ===")
        print(self.engine.display_info())
        print()

    def display_car_body_info(self):
        """Выводит информацию только о кузове"""
        print("=== Информация о кузове ===")
        print(self.car_body.display_info())
        print()

    def display_wheel_info(self):
        """Выводит информацию о всех колесах"""
        print("=== Информация о колесах ===")
        for i, wheel in enumerate(self.wheels, 1):
            print(f"Колесо {i}: {wheel.display_info()}")
        print()

    def display_full_info(self):
        """
        Выводит полную информацию об автомобиле
        Включает все компоненты и расчетную стоимость
        """
        print("=" * 50)
        print(f"АВТОМОБИЛЬ: {self.brand} {self.model} ({self.year} год)")
        print("=" * 50)
        print()
        self.display_engine_info()
        self.display_car_body_info()
        self.display_wheel_info()
        print(f"Общая стоимость автомобиля: ${self.estimate_price():,.2f}")
        print("-" * 50)

    # ========== БИЗНЕС-ЛОГИКА ==========
    def estimate_price(self):
        """
        Расчет приблизительной стоимости автомобиля
        Логика расчета:
        - Базовая цена: $20,000
        - Двигатель: $100 за каждую л.с.
        - Кузов: зависит от типа (см. словарь body_prices)
        - Колеса: $50 за каждый дюйм диаметра (умножается на 4)
        """
        base_price = 20000  # базовая цена

        # Расчет стоимости двигателя
        engine_price = self.engine.max_power * 100

        # Словарь стоимостей для разных типов кузова
        body_prices = {
            'седан': 5000,
            'хэтчбек': 4000,
            'внедорожник': 8000,
            'купе': 6000,
            'универсал': 4500
        }
        # Получение стоимости кузова (по умолчанию 5000)
        body_price = body_prices.get(self.car_body.body_type.lower(), 5000)

        # Расчет стоимости колес (берется диаметр первого колеса)
        wheel_price = self.wheels[0].diameter * 50

        # Итоговая стоимость
        return base_price + engine_price + body_price + wheel_price * 4

    def start_engine(self):
        """Имитирует запуск двигателя автомобиля"""
        print(f"Запускается двигатель {self.engine.max_power} л.с. на {self.engine.fuel_type}...")
        print("Двигатель запущен! Врум-врум!")
        print()

    def __str__(self):
        """Краткое строковое представление автомобиля"""
        return f"{self.brand} {self.model} ({self.year})"


# ==================== ТОЧКА ВХОДА ====================
# Демонстрация работы системы
# Создание различных конфигураций автомобилей
# =====================================================

if __name__ == "__main__":
    # Заголовок программы
    print("СИСТЕМА УПРАВЛЕНИЯ АВТОМОБИЛЬНОЙ КОМПАНИИ")
    print("=" * 50)

    # ---------- ПРИМЕР 1: ЭКОНОМНЫЙ СЕДАН ----------
    print("\n1. Создаем экономный седан:")
    engine1 = Engine(120, "бензин")
    body1 = CarBody("седан", 4)
    wheels1 = [Wheel(16, "летняя") for _ in range(4)]  # 4 одинаковых колеса

    car1 = Car("Toyota", "Corolla", 2023, engine1, body1, wheels1)
    car1.display_full_info()
    car1.start_engine()

    # ---------- ПРИМЕР 2: ВНЕДОРОЖНИК ----------
    print("\n2. Создаем внедорожник:")
    engine2 = Engine(250, "дизель")
    body2 = CarBody("внедорожник", 5)
    wheels2 = [Wheel(18, "всесезонная") for _ in range(4)]

    car2 = Car("Toyota", "Land Cruiser", 2023, engine2, body2, wheels2)
    car2.display_full_info()
    car2.start_engine()

    # ---------- ПРИМЕР 3: СПОРТИВНОЕ КУПЕ ----------
    print("\n3. Создаем спортивное купе:")
    engine3 = Engine(350, "бензин премиум")
    body3 = CarBody("купе", 2)
    wheels3 = [Wheel(19, "спортивная") for _ in range(4)]

    car3 = Car("Porsche", "911", 2023, engine3, body3, wheels3)
    car3.display_full_info()
    car3.start_engine()

    # ---------- ПРИМЕР 4: СЕМЕЙНЫЙ ХЭТЧБЕК ----------
    print("\n4. Создаем семейный хэтчбек:")
    engine4 = Engine(110, "газ/бензин")
    body4 = CarBody("хэтчбек", 5)
    wheels4 = [Wheel(15, "зимняя") for _ in range(4)]

    car4 = Car("Volkswagen", "Golf", 2023, engine4, body4, wheels4)
    car4.display_full_info()
    car4.start_engine()

    # ---------- ПРИМЕР 5: ЭЛЕКТРИЧЕСКИЙ АВТОМОБИЛЬ ----------
    print("\n5. Создаем электрический автомобиль:")
    engine5 = Engine(300, "электричество")
    body5 = CarBody("седан", 4)
    wheels5 = [Wheel(17, "эко-резина") for _ in range(4)]

    car5 = Car("Tesla", "Model 3", 2023, engine5, body5, wheels5)
    car5.display_full_info()
    car5.start_engine()

    # ========== ДЕМОНСТРАЦИЯ РАБОТЫ ОТДЕЛЬНЫХ МЕТОДОВ ==========
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ МЕТОДОВ:")
    print("=" * 50)

    print("\nИнформация только о двигателе Toyota Corolla:")
    car1.display_engine_info()

    print("\nИнформация только о кузове Porsche 911:")
    car3.display_car_body_info()

    print("\nИнформация только о колесах Volkswagen Golf:")
    car4.display_wheel_info()

    # ========== СРАВНЕНИЕ АВТОМОБИЛЕЙ ПО МОЩНОСТИ ==========
    print("\n" + "=" * 50)
    print("СРАВНЕНИЕ АВТОМОБИЛЕЙ ПО МОЩНОСТИ:")
    print("=" * 50)

    cars = [car1, car2, car3, car4, car5]
    for car in cars:
        print(f"{car.brand} {car.model}: {car.engine.max_power} л.с.")

    # Поиск самого мощного автомобиля
    most_powerful = max(cars, key=lambda c: c.engine.max_power)
    print(f"\nСамый мощный автомобиль: {most_powerful} ({most_powerful.engine.max_power} л.с.)")

