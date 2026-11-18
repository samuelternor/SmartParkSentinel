# M7 — Documented Refactor

## What Was Wrong

In my SmartPark Sentinel app, the main part of `sparking.py` was doing too many things. It was setting up the program, checking vehicles, saving information, and printing results.

This made the code harder to organize and reuse.

The code smell was called **Mixed Responsibilities**.

## What I Changed

I created a new function called `process_vehicles()`.

I moved the vehicle-processing loop into this function. It checks each vehicle, saves the result, and prints the vehicle status.

I did not change the `check_vehicle()` function or the existing tests.

## What Became Easier

My code is now easier to read because the vehicle-processing steps are grouped together.

I can also reuse the new function without copying the same loop.

## Testing

Before refactoring: 7 tests passed.

After refactoring: 7 tests passed.

The same tests were used both times without changing them.

This shows that the refactor did not break any behavior covered by the tests.