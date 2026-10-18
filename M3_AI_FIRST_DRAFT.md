
# SmartPark Sentinel — AI First Domain Model

## AI Tool
GitHub Copilot in VS Code

## Original AI-Generated ER Diagram

```mermaid
erDiagram
    VEHICLE {
        string vehicle_id PK
        string license_plate
        string make
        string model
        string color
    }

    REGISTRATION {
        string registration_id PK
        string vehicle_id FK
        date valid_from
        date valid_until
        string status
    }

    PARKING_SESSION {
        string session_id PK
        string vehicle_id FK
        string registration_id FK
        datetime entered_at
        datetime exited_at
        string observed_plate
        string status
    }

    SECURITY_ALERT {
        string alert_id PK
        string session_id FK
        string vehicle_id FK
        string watchlist_entry_id FK
        string alert_type
        datetime created_at
        string status
        string details
    }

    WATCHLIST_ENTRY {
        string watchlist_entry_id PK
        string license_plate
        string source
        datetime added_at
        datetime expires_at
        boolean active
    }

    VEHICLE ||--o{ REGISTRATION : has
    VEHICLE ||--o{ PARKING_SESSION : participates_in
    REGISTRATION o|--o{ PARKING_SESSION : may_cover
    PARKING_SESSION o|--o{ SECURITY_ALERT : generates
    VEHICLE o|--o{ SECURITY_ALERT : concerns
    WATCHLIST_ENTRY o|--o{ SECURITY_ALERT : may_trigger
```

## Original AI Assumptions

A vehicle can have multiple registrations over time and multiple parking sessions. A session may have no linked registration when the vehicle is unregistered or its registration cannot be matched.

`observed_plate` is kept on the session to preserve what the camera detected, including a missing or unreadable plate, while `license_plate` represents the vehicle's stored plate.

Alerts can lack a vehicle, session, or watchlist match when detection is incomplete or the alert has another cause.

A watchlist entry may trigger multiple alerts; its plate and source are stored independently of the vehicle record.
