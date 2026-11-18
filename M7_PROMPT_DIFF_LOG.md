# M7 — Prompt-and-Diff Log

## Project
SmartPark Sentinel

## AI Tool Used
GitHub Copilot in VS Code.

## Prompt Given to AI

I asked GitHub Copilot to refactor the vehicle-processing code in `sparking.py`.

I asked it to:
- Move the vehicle-processing loop into a separate function.
- Keep the application behavior the same.
- Leave `check_vehicle()` unchanged.
- Keep the database operations and printed output the same.
- Avoid changing the existing tests.
- Explain the code smell and show the changes.

## AI Suggestion

Copilot suggested creating a new function called `process_vehicles()`.

The function handles checking vehicles, saving their information, and printing their status.

## Changes Made

Before refactoring, the vehicle-processing loop was inside the main program.

After refactoring, the loop was moved into `process_vehicles()`.

The main program now calls this function instead of containing the loop directly.

## Testing

Before: 7 tests passed.

After: 7 tests passed.

No test files were changed.

## My Review

I reviewed the changes and confirmed that the vehicle-processing steps were moved into a separate function.

The refactor makes my code easier to understand and reuse.

The existing tests passed after the change, so the behavior covered by those tests was preserved.

## Diff Evidence

See `M7_REFACTOR_DIFF.txt` for the before-and-after code changes.