from abc import ABC
from .tires import Tires

class CarriganTires(Tires, ABC):
    def __init__(self, wear_array):
        self.wear_array = wear_array
        
    def needs_service(self):
        return max(self.wear_array) >= 0.9
