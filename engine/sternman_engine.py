from engine.Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, service_indicator: bool):
        self.service_indicator = service_indicator

    def needs_service(self):
        return self.service_indicator
