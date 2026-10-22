# IAP M6 — Prompt-and-Diff Log

**Project:** SmartPark Sentinel  
**Assignment:** M6 — Tests and Bug-Injection Demonstration  
**Date:** October 22, 2026

## 1. AI Tool Used

I used ChatGPT to help me create additional tests, generate a coverage report, and demonstrate how my tests detect an intentionally introduced bug.

## 2. Prompt and Goal

I asked ChatGPT to guide me step by step through IAP M6 using my existing SmartPark Sentinel Python application.

My goal was to test the vehicle security logic and the real SQLite database, then intentionally break one condition to verify that the test suite catches the mistake.

## 3. AI Suggestions and My Changes

| AI suggestion | What I changed or verified |
|---|---|
| Add a boundary test | Added `test_parking_exactly_24_hours` to `test_sparking.py`. |
| Test the complete application | Created `test_acceptance.py` to run the application and verify saved SQLite records. |
| Generate coverage | Installed `pytest-cov` and generated terminal and HTML coverage reports. |
| Inject a small bug | Temporarily changed `hours_parked >= 24` to `hours_parked > 24`. |
| Verify the tests detect the bug | Ran pytest and confirmed that the 24-hour boundary test failed. |
| Restore the correct behavior | Changed the condition back to `>= 24` and reran the tests. |

## 4. Test Results

Before the bug injection, all seven tests passed.

The tests included vehicle security unit tests, a database integration test, and an end-to-end acceptance test.

## 5. Coverage Report

I generated a coverage report using:

`python -m pytest --cov=sparking --cov=database --cov-report=term-missing --cov-report=html -v`

**Results:**

- `database.py`: 100% coverage
- `sparking.py`: 50% coverage
- Total coverage: 67%

The coverage report showed that database operations were fully exercised, while some application code was not counted as covered.

## 6. Bug-Injection Demonstration

I intentionally changed the parking-duration condition.

**Original code:**

`if hours_parked >= 24:`

**Injected fault:**

`if hours_parked > 24:`

The incorrect condition treated a vehicle parked for exactly 24 hours as normal instead of showing a warning.

I ran:

`python -m pytest -v`

**Result:** 1 failed, 6 passed.

The failing test was `test_parking_exactly_24_hours`.

I also used `git diff -- sparking.py` to inspect and capture the exact change.

## 7. Fix and Verification

I restored the original condition:

`if hours_parked >= 24:`

After running pytest again, all seven tests passed.

This demonstrated that the new boundary test detects a meaningful error in the parking security logic.

## 8. Reflection

AI helped me organize my test cases and understand how a small code change can introduce a user-visible problem.

The 24-hour boundary test was important because my earlier tests did not specifically check that exact value.

The bug-injection demonstration gave me evidence that the tests can detect an incorrect parking warning instead of only passing when the application works.