
# SmartPark Sentinel

## Project Concept

SmartPark Sentinel is an intelligent parking management and security system designed to improve vehicle safety and monitoring in parking facilities. The application will track vehicles entering and leaving a parking area, detect vehicles parked for unusually long periods, and identify vehicles that may have been abandoned for 30 days or more. It will also flag missing license plates, unknown vehicle registrations, and possible stolen vehicles by comparing license plate numbers with simulated or authorized watchlists. The system will eventually include camera-based vehicle detection, license plate recognition, security notifications, and an interactive monitoring dashboard.

## Technology Stack

- Python 3.13
- Streamlit (planned dashboard)
- SQLite (planned database)
- OpenCV (planned camera processing)
- YOLO (planned vehicle detection)
- OCR (planned license plate recognition)
- pytest (automated testing)
- pip (package manager)
- Git and GitHub (version control)

## Current Features

- Simulated stolen vehicle watchlist checking
- Missing license plate alerts
- Long-term parking alerts
- Normal vehicle identification
- Four automated tests

## How to Run

Run the program:

```bash
python sparking.py
```

Run the automated tests:

```bash
python -m pytest -v
```

## Future Development

The application will be expanded with vehicle registration, real-time parking monitoring, parking occupancy tracking, security dashboards, and camera-assisted vehicle identification. Security alerts will require human verification.

## Project Status

Milestone 1: Initial setup and toolchain verification.
