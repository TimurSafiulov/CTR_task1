class OnboardComputer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Бортовий комп'ютер запущено. Ініціалізація систем...")
        return cls._instance

if __name__ == "__main__":
    print("--- Тестування Singleton ---")
    comp1 = OnboardComputer()
    comp2 = OnboardComputer()
    
    print(f"Чи це один і той самий об'єкт комп'ютера? {comp1 is comp2}")