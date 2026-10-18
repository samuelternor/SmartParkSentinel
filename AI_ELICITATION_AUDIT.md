
# SmartPark Sentinel — AI Elicitation Audit

## 1. AI Tool Used

AI Tool: GitHub Copilot in VS Code

Purpose: To generate requirements independently
for my SmartPark Sentinel parking security system.

The original AI response is saved in
AI_GENERATED_REQUIREMENTS.md.

## 2. What the AI Got Right

GitHub Copilot correctly identified the main
features of my project, including:

- Registering vehicles at a parking facility.
- Recording vehicle entry and exit times.
- Detecting vehicles parked for 24 hours or longer.
- Flagging vehicles parked for 30 days or more.
- Identifying missing or unreadable license plates.
- Checking possible stolen vehicles against a
  simulated or authorized watchlist.
- Flagging vehicles without parking registration.
- Providing a security dashboard and alert management.

The AI also suggested useful improvements I had
not fully considered, such as preventing duplicate
active parking sessions, recording who resolves
alerts, and requiring manual verification of
possible stolen-vehicle matches.

These ideas could improve system reliability
and reduce false security alerts.

## 3. What the AI Missed

### Missing Requirement 1: Physical Vehicle Movement

My idea includes identifying cars that remain
parked in the same place for a month without moving.

The AI only tracked whether a parking session
remained open. A vehicle might move within the
facility without an exit being recorded.

The AI should have asked whether parking-space
sensors, cameras, or manual inspections would
be needed to confirm actual vehicle movement.

### Missing Requirement 2: Watchlist Updates

The AI described comparing plates against a
watchlist but did not establish how often the
watchlist should be updated or what happens
when the information is outdated.

This matters because an old record could
generate an incorrect stolen-vehicle alert.

### Missing Requirement 3: Camera Detection Failures

The AI mentioned unreadable plates and optional
camera integration, but did not define how the
system would handle camera outages, poor lighting,
or completely missed vehicle detections.

The system needs a manual entry method and a
way to identify missing observations.

### Missing Requirement 4: Alert Response Deadline

The AI suggested notifications and escalation
but did not establish a measurable time limit
for sending critical security alerts.

For example, a future requirement could state
that 95% of alerts must appear within 5 seconds
after an event is recorded.

## 4. What the AI Invented or Assumed

### Added Feature 1: Multiple Parking Facilities

The AI repeatedly introduced facility-specific
records and permissions.

My original project did not require monitoring
multiple facilities. I initially want the
system to work for one parking facility.

Decision: Defer multi-facility support.

### Added Feature 2: Reopening Resolved Alerts

The AI added the ability to reopen resolved
security alerts.

I requested alert detection and review, but
not an alert-reopening workflow.

Decision: Not required in the initial version.

### Added Feature 3: Configurable Parking Thresholds

The AI suggested configurable alert thresholds.

I originally specified long-parking warnings
and a 30-day monitoring condition. I did not
ask for staff to change those thresholds.

Decision: Keep fixed thresholds for the initial
version and consider configuration later.

### Added Feature 4: Reports and Exports

The AI suggested downloadable audit reports
and role-based exports.

I did not request export functionality as part
of the first version.

Decision: Defer report exports until the core
monitoring and alert features work.

## 5. Engineering Judgment

GitHub Copilot produced a useful starting
requirements list, but I would not accept
everything without reviewing it.

The AI correctly captured most of my system's
main features and improved the requirements
with ideas such as manual verification,
duplicate detection, and accountability.

However, it did not fully address my requirement
to identify cars that physically remain parked
without movement for a month. It also left
important operational questions unanswered,
including watchlist freshness and camera failures.

Some additional features were reasonable ideas,
but they were not part of my original scope.
Adding all of them now would make the project
more complicated than necessary.

My decision is to keep the core parking security
features, add safeguards against false alerts,
and postpone multi-facility support and exports.

## 6. Conclusion

This exercise showed me that AI can help generate
requirements quickly, but its suggestions must
be checked against the actual project goals.

I will use the AI output as a starting point,
not as the final authority on system requirements.
