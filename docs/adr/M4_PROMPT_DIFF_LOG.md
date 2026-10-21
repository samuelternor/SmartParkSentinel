# IAP M4 — Prompt-and-Diff Log

**Project:** SmartPark Sentinel  
**Assignment:** M4 — ADR-001  
**Date:** October 21, 2026

## 1. AI Tool Used

I used ChatGPT to help organize and write my architecture decision record.

## 2. Prompt Given to AI

I asked ChatGPT to help me complete IAP M4 by writing an ADR for my SmartPark Sentinel parking security project.

The decision was about connecting security alerts to parking sessions instead of only connecting them to vehicles.

## 3. AI-Generated Suggestions

ChatGPT suggested including:

- The problem that made the architecture decision necessary.
- The decision to link security alerts to parking sessions.
- Two alternative designs.
- The positive and negative consequences of the decision.

## 4. Changes and Review

The following describes the draft and my review of it:

| AI suggestion | My review or change |
|---|---|
| Link alerts to parking sessions | This matches the design used in my M3 domain model. |
| Connect alerts directly to vehicles only | I considered this alternative but it would not clearly identify individual parking visits. |
| Keep alerts independent of parking sessions and vehicles | I rejected this because it would make investigations more difficult. |
| Include negative consequences | I included added database complexity and more difficult queries. |

## 5. Final Decision

My ADR documents the decision to connect security alerts to parking sessions while allowing optional references to vehicles and watchlist entries.

I chose this design to keep better records of security incidents and make investigations easier.

## 6. Files Created

- `docs/adr/ADR-001.md`
- `docs/adr/M4_PROMPT_DIFF_LOG.md`

## 7. Reflection

AI helped me organize my architecture decision and identify its tradeoffs. The final ADR reflects the design selected for my SmartPark Sentinel project.