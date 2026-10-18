
# SmartPark Sentinel — M3 AI Domain Model Critique

## 1. Introduction

For Milestone 3, I asked GitHub Copilot to create
an ER diagram for my SmartPark Sentinel project.

I saved its original draft in M3_AI_FIRST_DRAFT.md
and created my revised model in M3_DOMAIN_MODEL.md.

I compared both diagrams against my Milestone 2
requirements to identify unnecessary complexity,
missing information, and unsupported assumptions.

## 2. What the AI Got Right

Copilot correctly identified five important entities:

- VEHICLE
- REGISTRATION
- PARKING_SESSION
- SECURITY_ALERT
- WATCHLIST_ENTRY

These entities support my main requirements.

VEHICLE and REGISTRATION support vehicle
registration (US-01).

PARKING_SESSION supports entry and exit tracking
(US-02) and long-term parking detection (US-03).

WATCHLIST_ENTRY and SECURITY_ALERT support
possible stolen-vehicle alerts (US-05).

I also agree with Copilot's decision to store
observed_plate separately from the vehicle's
registered license_plate.

This is useful when a camera cannot read a plate
or a vehicle has no visible plate.

## 3. Where the AI Over-Modeled

Copilot added three possible foreign keys to
SECURITY_ALERT: session_id, vehicle_id, and
watchlist_entry_id.

The direct relationship between VEHICLE and
SECURITY_ALERT duplicates information that can
normally be obtained through PARKING_SESSION.

For my initial project, I removed vehicle_id
from SECURITY_ALERT to simplify the model.

Copilot also connected REGISTRATION directly
to PARKING_SESSION using registration_id.

I removed this relationship because my current
requirements do not require saving which specific
registration version covered every session.

Both links could become useful later, but they
add complexity to the initial design.

## 4. Where the AI Under-Modeled

### Missing Plate Status

Copilot included observed_plate but did not
include a separate field describing whether
the plate was readable, missing, or unreadable.

My revised model adds plate_status to
PARKING_SESSION.

This directly supports US-04.

### Missing Parking Space Information

Copilot tracked entry and exit timestamps but
did not record the parking space.

My project is especially concerned with vehicles
parked for 30 days or longer without moving.

I added parking_space to PARKING_SESSION.

However, a single parking_space value is not
enough to prove that a vehicle never moved.
Future versions may require repeated observations
or manual inspections.

### Missing Alert Resolution Details

Copilot's SECURITY_ALERT included a status,
but no resolution timestamp or resolution reason.

My model adds resolved_at and resolution_reason.

These support US-08 by allowing security staff
to document how alerts were resolved.

## 5. Unsupported Relationship Assumptions

Copilot assumed that a parking session could
be linked to a specific REGISTRATION record.

Although this is a reasonable design, my
Milestone 2 requirements did not establish
that historical registration versions must
be associated with parking sessions.

I therefore removed that relationship from
the initial model.

Copilot also permitted alerts to reference
a VEHICLE independently of a parking session.

I chose to associate alerts with a parking
session to simplify the first version.

This decision means the current model does not
fully support standalone alerts that occur
outside a parking session. That limitation
must be revisited if future requirements
include those cases.

## 6. Why My Model Is Different

My revised model keeps the same five core
entities but makes these structural changes:

1. Removed the direct VEHICLE to SECURITY_ALERT
   relationship and vehicle_id foreign key.

2. Removed registration_id from PARKING_SESSION
   and the direct REGISTRATION relationship.

3. Added plate_status to PARKING_SESSION.

4. Added parking_space to PARKING_SESSION.

5. Added resolved_at and resolution_reason
   to SECURITY_ALERT.

These choices prioritize the main parking
monitoring and alert features over extra
relationships that are not yet required.

## 7. Remaining Limitations

My revised model is not perfect.

It does not separately model staff accounts
or identify which employee resolved an alert.

It also does not fully model multiple parking
spaces, camera observations, or physically
verified vehicle movement.

These requirements need further refinement
before a production system is developed.

## 8. Engineering Judgment

I would not accept Copilot's first draft
without reviewing it.

Its core entities were useful, but some
relationships were more detailed than my
initial application required.

At the same time, it missed important
information about plate visibility, parking
location, and alert resolution.

My revised diagram provides a simpler
starting point for SmartPark Sentinel while
making the current design limitations clear.

The AI model was helpful as a first draft,
but the final design should be driven by
the application's actual requirements.
