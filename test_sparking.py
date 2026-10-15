
from sparking import check_vehicle

def test_stolen_vehicle():
    assert check_vehicle("ABC123", 2, {"ABC123"}) == "ALERT: Possible stolen vehicle"

def test_missing_plate():
    assert check_vehicle("", 3, set()) == "ALERT: Missing license plate"

def test_long_parking():
    assert check_vehicle("MEM456", 750, set()) == "ALERT: Vehicle parked for 30+ days"

def test_normal_vehicle():
    assert check_vehicle("PARK123", 5, set()) == "Vehicle status: Normal"
