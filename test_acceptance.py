
import os
import sqlite3
import subprocess
import sys
from pathlib import Path


def test_vehicle_registration_end_to_end(tmp_path):
    app = Path(__file__).parent / "sparking.py"
    database_file = tmp_path / "smartpark.db"

    result = subprocess.run(
        [sys.executable, str(app)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True,
    )

    # Check what the user sees
    assert "SMARTPARK SENTINEL" in result.stdout
    assert "VEHICLES SAVED IN DATABASE" in result.stdout
    assert "ALERT: Missing license plate" in result.stdout

    # Check real database storage
    assert database_file.exists()

    with sqlite3.connect(database_file) as connection:
        rows = connection.execute(
            "SELECT plate, hours_parked, status FROM vehicles ORDER BY id"
        ).fetchall()

    assert len(rows) == 4
    assert rows[0] == (
        "ABC123", 2, "ALERT: Possible stolen vehicle"
    )
    assert rows[1] == (
        "", 3, "ALERT: Missing license plate"
    )
    assert rows[2] == (
        "MEM456", 750, "ALERT: Vehicle parked for 30+ days"
    )
    assert rows[3] == (
        "PARK123", 5, "Vehicle status: Normal"
    )
