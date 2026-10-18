
# SmartPark Sentinel — Requirements Document

## Project Description

SmartPark Sentinel is a smart parking security system
designed to monitor vehicles entering and leaving
parking facilities. It will help security staff
identify possible stolen vehicles, missing license
plates, unregistered vehicles, and vehicles parked
for unusually long periods, including 30 days or more.

## User Stories and Acceptance Criteria

### US-01: Vehicle Registration
As a parking administrator, I want to register
vehicles so that I can identify authorized vehicles.

Acceptance Criteria:
- The administrator can add a vehicle's plate number.
- Vehicle registration information is saved.
- Duplicate plate numbers are flagged.

### US-02: Vehicle Entry and Exit
As a security officer, I want to track vehicle
entry and exit so that I know how long each car
has been parked.

Acceptance Criteria:
- The system records vehicle entry times.
- The system records vehicle exit times.
- Parking duration is automatically calculated.

### US-03: Long-Term Parking Detection
As a security officer, I want to identify vehicles
parked too long so that I can investigate them.

Acceptance Criteria:
- A warning is created after 24 hours.
- A 30-day alert is created after 720 hours.
- Alerts display the vehicle and parking duration.

### US-04: Missing License Plates
As a security officer, I want to identify vehicles
without visible plates so that they can be inspected.

Acceptance Criteria:
- Vehicles with missing plates are flagged.
- Unreadable plates are sent for manual review.
- Security staff can record inspection results.

### US-05: Possible Stolen Vehicles
As a security officer, I want to compare detected
plates with an authorized watchlist so that I can
identify possible stolen vehicles.

Acceptance Criteria:
- Plates are checked against a simulated or
  authorized watchlist.
- Possible matches generate an alert.
- Security staff must verify matches manually.

### US-06: Unregistered Vehicles
As a parking administrator, I want to identify
vehicles without parking registration so that I
can review their authorization.

Acceptance Criteria:
- Plates are checked against facility registrations.
- Unknown plates generate a notification.
- Staff can approve or reject registration requests.

### US-07: Monitoring Dashboard
As a security officer, I want a dashboard so that
I can monitor parking activity in one place.

Acceptance Criteria:
- The dashboard shows available parking spaces.
- Active security alerts are displayed.
- Vehicle parking history can be viewed.

### US-08: Security Alert Management
As a security supervisor, I want to review and
resolve alerts so that false alarms can be cleared.

Acceptance Criteria:
- Alerts have open and resolved statuses.
- Authorized staff can close an alert.
- Alert resolutions are saved with timestamps.

## Non-Functional Requirements

### NFR-01: Performance
For 500 simulated vehicle records, at least 95%
of 100 vehicle status checks must finish within
2 seconds each.

### NFR-02: Accuracy
The system must correctly classify all 20
predefined test scenarios for missing plates,
watchlist matches, long parking, and normal vehicles.

### NFR-03: Security
Unauthenticated users must be denied access
to vehicle records and security alerts in
100% of 20 predefined access-control tests.

## Project Scope

The initial version uses simulated vehicle data.
Future versions will include an interactive
dashboard, SQLite storage, and camera-assisted
vehicle identification.
