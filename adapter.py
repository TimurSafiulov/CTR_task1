class StationType2:
    def charge_type2(self):
        return "Подаю струм через європейський роз'єм Type 2"

class AdapterType1(StationType2):
    def charge_type1(self):
        power = self.charge_type2()
        return f"{power} -> [Адаптер] -> Перетворено для американського роз'єму Type 1"

if __name__ == "__main__":
    print("--- Тестування Adapter ---")
    adapter = AdapterType1()
    
    print("Підключаємо авто до станції через адаптер:")
    print(adapter.charge_type1())