
# SmartPark Sentinel — M3 Prompt and Diff Log

## AI Tool Used
GitHub Copilot in VS Code

## First Prompt
I am developing SmartPark Sentinel, a parking
security system. Using the requirements in
REQUIREMENTS.md, create an initial domain model
as a Mermaid ER diagram. Include entities,
attributes, primary keys, foreign keys,
relationships, and cardinalities. Explain your
design assumptions. Do not create or modify
any files. I need to preserve your first draft
for an academic critique.

## First AI Response
Copilot replied that it could only suggest
project directory structures. No domain
model was produced from the first prompt.

## Second Prompt
Create a Mermaid ER diagram for SmartPark Sentinel,
a parking security application.

Include Vehicle, Registration, ParkingSession,
SecurityAlert, and WatchlistEntry entities with
their attributes, primary keys, foreign keys,
and relationships.

Explain your assumptions. Respond with Mermaid
diagram text only, followed by your explanation.
Do not create or edit any files.

## Second AI Response
Copilot generated an ER diagram with five
entities and their relationships.

The original model was preserved in
M3_AI_FIRST_DRAFT.md.

## Follow-up Prompt
Please provide the exact Mermaid source code
for the ER diagram you just generated.
Do not change or redesign anything.
Include the original assumptions.

## Changes from the AI Draft
- Removed the direct VEHICLE-to-SECURITY_ALERT link.
- Removed registration_id from PARKING_SESSION.
- Added plate_status to PARKING_SESSION.
- Added parking_space to PARKING_SESSION.
- Added resolved_at to SECURITY_ALERT.
- Added resolution_reason to SECURITY_ALERT.
- Adjusted the vehicle relationship to allow
  parking sessions without a known vehicle.

## Files Created
- M3_AI_FIRST_DRAFT.md
- M3_DOMAIN_MODEL.md
- M3_Domain_Model.png
- M3_AI_CRITIQUE.md
- M3_PROMPT_DIFF_LOG.md

## Code Diff
No Python application code was changed.
Changes were limited to documentation and
the ER diagram image.

## Engineering Judgment
I kept the core domain entities but simplified
unnecessary relationships and added attributes
needed for missing plates, parking monitoring,
and alert resolution.
