from datetime import datetime, timedelta

def check_vehicle(plate, hours_parked, stolen_plates):
    if not plate:
        return "ALERT: Missing license plate"

    if plate.upper() in stolen_plates:
        return "ALERT: Possible stolen vehicle"

    if hours_parked >= 720:
        return "ALERT: Vehicle parked for 30+ days"

    if hours_parked >= 24:
        return "WARNING: Vehicle parked too long"

    return "Vehicle status: Normal"


if __name__ == "__main__":
    stolen_plates = {"ABC123", "XYZ789"}

    print("SMARTPARK SENTINEL")
    print("------------------")

    vehicles = [
        ("ABC123", 2),
        ("", 3),
        ("MEM456", 750),
        ("PARK123", 5),
    ]

    for plate, hours in vehicles:
        status = check_vehicle(plate, hours, stolen_plates)
        print(f"Plate: {plate or 'UNKNOWN'} | {status}")