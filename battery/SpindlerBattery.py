from datetime import date
from battery.Battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self) -> bool:
        service_date: date.year = 2
        return self._current_date.year - self._last_service_date.year >= service_date
