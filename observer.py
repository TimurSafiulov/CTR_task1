class Battery12V:
    def __init__(self):
        self.subscribers = []
        self.voltage = 12.5

    def attach(self, sub):
        self.subscribers.append(sub)

    def set_voltage(self, voltage):
        self.voltage = voltage
        print(f"\n[Батарея] Поточна напруга: {self.voltage}V")
        if self.voltage < 11.5:
            self.notify_drop()

    def notify_drop(self):
        for sub in self.subscribers:
            sub.update()

class Dashboard:
    def update(self):
        print("[Приладова панель] Помилка: Service EV System!")

class MobileApp:
    def update(self):
        print("[Мобільний додаток] Push-сповіщення: Критично низький заряд 12V батареї!")

if __name__ == "__main__":

    print("--- Тестування Observer ---")
    battery = Battery12V()
    
    battery.attach(Dashboard())
    battery.attach(MobileApp())

    battery.set_voltage(12.0) 
    battery.set_voltage(11.0) 