
import database
from sparking import check_vehicle


def test_database_save_and_retrieve(tmp_path, monkeypatch):
    # Use a real temporary SQLite database
    db_file = tmp_path / "test_smartpark.db"
    monkeypatch.setattr(database, "DATABASE_NAME", str(db_file))

    # Create the database
    database.create_database()

    # Check the vehicle
    plate = "TEST123"
    hours = 30
    status = check_vehicle(plate, hours, set())

    # Save the vehicle
    vehicle_id = database.add_vehicle(plate, hours, status)

    # Retrieve the saved vehicle
    vehicles = database.get_vehicles()

    # Verify the database
    assert db_file.exists()
    assert len(vehicles) == 1
    assert vehicles[0] == (vehicle_id, plate, hours, status)
    assert status == "WARNING: Vehicle parked too long"
