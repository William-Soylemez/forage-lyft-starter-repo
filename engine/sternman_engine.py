from abc import ABC
from .engine import Engine

class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on
        
    def engine_should_be_serviced(self):
        return self.warning_light_on
