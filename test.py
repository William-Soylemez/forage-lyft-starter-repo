import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestNubbinBattery(unittest.TestCase):
    def create_and_test_battery(self, age, max_age):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - age)
        battery = NubbinBattery(last_service_date, today)
        self.assertEqual(battery.needs_service(), age > max_age)

    def test_new_battery(self):
        self.create_and_test_battery(0, 4)
    
    def test_one_year_old_battery(self):
        self.create_and_test_battery(1, 4)

    def test_two_year_old_battery(self):
        self.create_and_test_battery(2, 4)
    
    def test_four_year_old_battery(self):
        self.create_and_test_battery(4, 4)
    
    def test_five_year_old_battery(self):
        self.create_and_test_battery(5, 4)

class TestSpindler(unittest.TestCase):
    def create_and_test_battery(self, age, max_age):
        today = datetime.today()
        last_service_date = today.replace(year=today.year - age)
        battery = SpindlerBattery(last_service_date, today)
        self.assertEqual(battery.needs_service(), age > max_age)

    def test_new_battery(self):
        self.create_and_test_battery(0, 3)
    
    def test_one_year_old_battery(self):
        self.create_and_test_battery(1, 3)

    def test_two_year_old_battery(self):
        self.create_and_test_battery(2, 3)
    
    def test_four_year_old_battery(self):
        self.create_and_test_battery(4, 3)
    
    def test_five_year_old_battery(self):
        self.create_and_test_battery(5, 3)

class TestCapuletEngine(unittest.TestCase):
    def create_and_test_engine(self, mileage, last_service_mileage, max_mileage):
        engine = CapuletEngine(last_service_mileage, mileage)
        self.assertEqual(engine.needs_service(), mileage - last_service_mileage > max_mileage)

    def test_new_engine(self):
        self.create_and_test_engine(0, 0, 30000)
    
    def test_15000_mile_engine(self):
        self.create_and_test_engine(15000, 0, 30000)
    
    def test_30000_mile_engine(self):
        self.create_and_test_engine(30000, 0, 30000)
    
    def test_45000_mile_engine(self):
        self.create_and_test_engine(45000, 0, 30000)
    
    def test_old_service_engine(self):
        self.create_and_test_engine(60000, 30000, 30000)
    
    def test_old_unserviced_engine(self):
        self.create_and_test_engine(70000, 30000, 30000)

class TestWilloughbyEngine(unittest.TestCase):
    def create_and_test_engine(self, mileage, last_service_mileage, max_mileage):
        engine = WilloughbyEngine(last_service_mileage, mileage)
        self.assertEqual(engine.needs_service(), mileage - last_service_mileage > max_mileage)

    def test_new_engine(self):
        self.create_and_test_engine(0, 0, 60000)
    
    def test_15000_mile_engine(self):
        self.create_and_test_engine(15000, 0, 60000)
    
    def test_30000_mile_engine(self):
        self.create_and_test_engine(30000, 0, 60000)
    
    def test_60000_mile_engine(self):
        self.create_and_test_engine(60000, 0, 60000)
    
    def test_75000_mile_engine(self):
        self.create_and_test_engine(75000, 0, 60000)
    
    def test_old_service_engine(self):
        self.create_and_test_engine(60000, 30000, 60000)
    
    def test_old_unserviced_engine(self):
        self.create_and_test_engine(100000, 30000, 60000)

class TestSternmanEngine(unittest.TestCase):
    def create_and_test_engine(self, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        self.assertEqual(engine.needs_service(), warning_light_on)
    
    def test_needs_service(self):
        self.create_and_test_engine(True)
    
    def test_does_not_need_service(self):
        self.create_and_test_engine(False)

class TestCarriganTires(unittest.TestCase):
    def create_and_test_tires(self, wear_array):
        tires = CarriganTires(wear_array)
        self.assertEqual(tires.needs_service(), max(wear_array) >= 0.9)
    
    def test_needs_service(self):
        self.create_and_test_tires([0.8, 0.9, 0.8, 0.8])
    
    def test_does_not_need_service(self):
        self.create_and_test_tires([0.8, 0.8, 0.8, 0.8])

class TestOctoprimeTires(unittest.TestCase):
    def create_and_test_tires(self, wear_array):
        tires = OctoprimeTires(wear_array)
        self.assertEqual(tires.needs_service(), sum(wear_array) >= 3)
    
    def test_needs_service(self):
        self.create_and_test_tires([0.7, 0.7, 0.8, 0.8])
    
    def test_does_not_need_service(self):
        self.create_and_test_tires([0.7, 0.7, 0.7, 0.7])

if __name__ == '__main__':
    unittest.main()
