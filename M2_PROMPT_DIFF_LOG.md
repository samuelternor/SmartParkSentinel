
# SmartPark Sentinel — M2 Prompt and Diff Log

## Milestone 2: Requirements and AI Elicitation Audit

### AI Tool
GitHub Copilot in VS Code

### Prompt Used
I am developing SmartPark Sentinel, a parking
security system. It should monitor cars entering
and leaving, detect vehicles parked too long,
flag cars parked for 30 days or more without
leaving, identify missing license plates and
vehicles without parking registration, and flag
possible stolen vehicles using a simulated or
authorized watchlist.

Act as a requirements engineer. Generate 8 user
stories with acceptance criteria and 3 measurable
non-functional requirements. Identify assumptions,
suggest additional features, and ask questions
about missing requirements. Do not read or modify
my existing requirements file or other project files.

### AI Output
GitHub Copilot generated 8 user stories, 3 measurable
non-functional requirements, assumptions, suggested
additional features, and clarification questions.

The complete response is preserved in
AI_GENERATED_REQUIREMENTS.md.

### Code Diff
No Python source code was changed by the AI tool.

### Documentation Changes
- Created REQUIREMENTS.md with project requirements.
- Created AI_GENERATED_REQUIREMENTS.md containing
  the original Copilot response.
- Created AI_ELICITATION_AUDIT.md comparing Copilot's
  output with the intended project requirements.
- Created M2_PROMPT_DIFF_LOG.md to document AI use.

### Engineering Decision
I reviewed Copilot's suggestions instead of accepting
them automatically. I identified missing details about
physical vehicle movement, watchlist updates, camera
failures, and alert timing.

I also identified additional features that were not
part of my original project scope, such as supporting
multiple facilities and exporting reports.

The existing Python implementation was left unchanged.
