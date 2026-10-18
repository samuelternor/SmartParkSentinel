User: I am developing SmartPark Sentinel, a parking security system. It should monitor cars entering and leaving, detect vehicles parked too long, flag cars parked for 30 days or more without leaving, identify missing license plates and vehicles without parking registration, and flag possible stolen vehicles using a simulated or authorized watchlist.

Act as a requirements engineer. Generate 8 user stories with acceptance criteria and 3 measurable non-functional requirements. Identify assumptions, suggest additional features, and ask questions about missing requirements. Do not read or modify my existing requirements file or other project files.

GitHub Copilot: # SmartPark Sentinel Requirements

## User Stories and Acceptance Criteria

### US-01: Register Vehicles
As a parking administrator, I want to register vehicles so that authorized vehicles can be identified.

- Staff can create and update a registration with a plate number and facility.
- Plate numbers are normalized before comparison.
- Duplicate active registrations are flagged and cannot be silently added.
- Registration changes are timestamped and attributable to a staff account.

### US-02: Record Vehicle Entry and Exit
As a security officer, I want to record vehicle movements so that parking activity and duration can be tracked.

- Each entry records the vehicle or observed plate, facility, and timestamp.
- Each exit records the matching active parking session and timestamp.
- The system calculates session duration from entry and exit times.
- A vehicle cannot have multiple active sessions at the same facility unless an authorized override is recorded.

### US-03: Detect Long-Term Parking
As a security officer, I want vehicles parked beyond configured thresholds flagged so that they can be investigated.

- An open parking session triggers an alert when it reaches the configured warning threshold.
- An open session triggers a distinct alert when it reaches 30 days (720 hours).
- Alerts show the vehicle or observed plate, entry time, elapsed duration, and threshold crossed.
- Alerts are not cleared merely by restarting the system; they are updated or resolved based on session status.

### US-04: Flag Missing or Unreadable Plates
As a security officer, I want plate visibility issues recorded so that affected vehicles can be inspected.

- Staff can record a vehicle observation as “missing plate” or “unreadable plate.”
- Missing-plate observations create an alert; unreadable observations are routed for manual review.
- Staff can add inspection notes and record the inspection outcome.
- The observation, reviewer, and timestamps are retained.

### US-05: Check a Watchlist
As a security officer, I want observed plates checked against an authorized watchlist so that possible matches can be reviewed.

- The system compares normalized observed plates with the configured watchlist.
- A possible match creates an alert showing the match basis and source.
- A match is marked as unverified until an authorized staff member reviews it.
- Staff can record a verification decision and its rationale; the system does not automatically take enforcement action.

### US-06: Identify Unregistered Vehicles
As a parking administrator, I want observed plates checked against facility registrations so that unauthorized or unknown vehicles can be reviewed.

- The system checks each readable observed plate against registrations for the relevant facility.
- Plates without a matching active registration create a notification or review item.
- Staff can approve or reject a registration request and record a reason.
- An unreadable plate is not classified as unregistered solely because it could not be matched.

### US-07: Monitor Parking Activity
As a security officer, I want a dashboard of current parking activity so that I can identify issues quickly.

- The dashboard shows configured capacity, occupied spaces, and available spaces.
- It displays active alerts with type, vehicle or plate, duration, and status.
- Staff can view a vehicle’s entry and exit history, subject to access permissions.
- Counts and alerts reflect the latest successfully recorded events and show when they were last updated.

### US-08: Review and Resolve Alerts
As a security supervisor, I want to manage alerts so that findings can be investigated and false alarms resolved.

- Alerts have open and resolved states and include a type, creation time, and associated event or vehicle.
- Authorized staff can resolve an alert with a resolution reason.
- Resolution records include the staff member and timestamp.
- Resolved alerts remain available for audit and can be reopened by authorized staff.

## Non-Functional Requirements

1. **Performance:** With 500 simulated vehicle records, at least 95 of 100 status checks must complete within 2 seconds on the agreed test environment.
2. **Classification accuracy:** The system must correctly classify all 20 agreed test scenarios covering missing and unreadable plates, watchlist matches, unregistered vehicles, long-term parking, and normal vehicles.
3. **Access control:** In 20 agreed access-control tests, every unauthenticated attempt to access vehicle records or security alerts must be denied.

## Assumptions

- The initial release uses simulated vehicle and watchlist data; watchlist use is authorized and configured by the organization.
- Plate comparisons use normalization rules appropriate to the facilities served.
- The 30-day threshold means 720 elapsed hours from the recorded entry time, without an intervening exit.
- Staff accounts and role assignments are available, and actions that change records or resolve alerts are auditable.
- Parking capacity and availability can be calculated from configured capacity and active sessions, unless sensors provide occupancy data.

## Suggested Additional Features

- Configurable alert thresholds, facility hours, and notification routing.
- Duplicate or out-of-order entry/exit detection with correction workflows.
- Alert prioritization, assignment, escalation, and notifications.
- Audit reports and exports with role-based access.
- Data retention controls and privacy safeguards for plate and watchlist data.
- Optional camera integration with confidence scores and human review.

## Questions About Missing Requirements

1. Which staff roles and permissions are needed, and who can access watchlist data?
2. What plate formats, normalization rules, and facilities must be supported?
3. Should long-term warnings repeat or escalate, and what happens when a vehicle exits and re-enters?
4. How should capacity and occupancy be determined when entry/exit events are missing or incorrect?
5. What registration-request workflow, notification channels, and response times are expected?
6. What data-retention periods, audit requirements, and privacy constraints apply?
7. What test environment and measurement method should be used for the performance requirement?