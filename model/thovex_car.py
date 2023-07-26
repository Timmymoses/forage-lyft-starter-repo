from datetime import datetime, date

from battery.Battery import Battery
from battery.NubbinBattery import NubbinBattery
from car_models.Car import Car
from engine.Engine import Engine
from engine.capulet_engine import CapuletEngine


class ThovexCar(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.battery: Battery = NubbinBattery(last_service_date, current_date)
        self.engine: Engine = CapuletEngine(last_service_mileage, current_mileage)
        super().__init__(self.battery, self.engine)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()

