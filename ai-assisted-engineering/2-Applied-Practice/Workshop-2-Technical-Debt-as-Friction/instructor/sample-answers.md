# Workshop 2 — Sample Answer Guidance

Use these notes when reviewing participant work on the Friction Map and Debt Inventory exercise.

## Strong Workshop 2 friction maps usually include

- **Repeated pain points instead of one-off annoyances.** The item describes something that is paid every PR, every release, every onboarding, or every incident — not a single bad week.
- **Prioritization based on change cost.** The top-ranked items are the ones that most often slow or block a routine change, not the ones that are most aesthetically offensive.
- **Evidence that participants can separate symptoms from root causes.** "Tests are flaky" is a symptom; the root cause might be environment debt (shared test database) or data debt (no stable seed fixtures).
- **At least one non-code debt item in the top priorities.** A top-three that is all code debt is a warning sign — the participant may still be equating debt with messy code. Strong answers include environment, release, observability, workflow, or knowledge debt in the top tier.
- **Operational specificity.** The estimated interest names who pays, how often, and roughly how much time — not just "this is painful."

## Strong classification answers

- Use the nine-category taxonomy consistently. "Setup only works on one machine" is environment debt, not knowledge debt — even though docs could reduce the symptom.
- Flag items that span categories (e.g., "no deployed-version endpoint" is simultaneously release debt and observability debt). Spanning categories is often a signal of high priority.
- Admit uncertainty when they have not yet confirmed a root cause.

## Example of a strong top-three pick

> **1. No reproducible local setup (environment debt).** Every new engineer loses ~2 days; senior engineers lose ~30 min per week helping. Staged improvement: add a devcontainer or make-based setup script for the most-edited service first.
>
> **2. No correlation IDs in logs (observability debt).** Every production incident requires grepping across three services. Quick-win candidate: add request-ID middleware and propagate through the two most-called services.
>
> **3. Manual release checklist in Slack (release + workflow debt).** Every release pays 30–60 min and relies on one engineer remembering the steps. Staged improvement: move the checklist into a reviewable script, then into CI.

Each item: specific, names the category, quantifies the interest, proposes a sized next step.

## Common weak patterns

These show up across the course, not just in this workshop, but they are especially common in Workshop 2 work.

- **Treating architecture as optional.** Participants skip design debt because it feels abstract. Push them to name a specific case where unclear boundaries slowed a recent change.
- **Using "AI should fix this" as a substitute for prioritization.** AI can help classify and draft, but it does not decide which debt is worth paying down. Reject top-three lists that hand the ranking to AI.
- **Confusing lots of text with good documentation.** A long README is not evidence that knowledge debt is low. Ask whether the doc is current, trustworthy, and operational.
- **Equating coverage with confidence.** "We have 85% coverage so quality debt is low" — no. Ask whether the tests fail when the behavior breaks.
- **Proposing big rewrites instead of staged improvements.** If a participant's top-three includes "rewrite the monolith," ask for a three-step version of that plan that could ship in 30 days.
- **Ignoring operations and deployment visibility.** A top-three with no observability or release debt in it is often missing the highest-interest items in the team's environment.
- **Symptom mixing.** "Things are slow" is not a debt item. Slowness is evidence; the debt is the underlying reproducibility, environment, or data problem.

## Reviewer checklist

When reviewing a group's submitted friction map, ask:

- Is every item operationally specific?
- Is the interest quantified (time, frequency, who pays)?
- Does the top three include at least one non-code debt item?
- Can the participant separate this item's symptom from its root cause?
- Is the proposed next step sized for staged improvement, not rewrite fantasy?
