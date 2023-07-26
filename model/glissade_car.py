from datetime import datetime, date

from battery.Battery import Battery
from battery.SpindlerBattery import SpindlerBattery
from car_models.Car import Car
from engine.Engine import Engine
from engine.willoughby_engine import WilloughbyEngine


class GlissadeCar(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.battery: Battery = SpindlerBattery(last_service_date, current_date)
        self.engine: Engine = WilloughbyEngine(last_service_mileage, current_mileage)
        super().__init__(self.battery, self.engine)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()

