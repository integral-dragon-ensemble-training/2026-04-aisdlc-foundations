# Workshop 2 — Resources

Curated readings to support Workshop 2: Technical Debt as Friction. These sources sharpen the distinction between local code smells and broader project debt, ground the "interest" metaphor in operational reality, and give participants a vocabulary for documenting engineering quality.

---

## Core readings

### Martin Fowler — Code Smell

Link: https://martinfowler.com/bliki/CodeSmell.html

Why use it:

- Useful for distinguishing local code smells from broader project debt.
- Helps participants see that a smell is a surface-level hint, not the whole problem.
- Pairs well with the "Smell or Debt?" lightweight activity.

### Twelve-Factor App

Link: https://12factor.net/

Why use it:

- Especially useful for configuration, dev/prod parity, logs, and operational discipline.
- Names the non-code categories of debt — environment, release, observability — in a concise, widely-cited form.
- A strong reference when discussing why "it works on my machine" is debt, not a quirk.

### Principles of Technical Documentation (arc42)

Link: https://arc42.org/principles-of-technical-documentation

Why use it:

- Good source for explaining why documentation quality is part of engineering quality.
- Supports the framing that knowledge debt is first-class debt, not a nice-to-have.
- Practical, implementation-agnostic, and compatible with how most teams actually work.

---

## Supplementary reading (optional)

### Martin Fowler — Technical Debt

Link: https://martinfowler.com/bliki/TechnicalDebt.html

Why use it:

- Foundational framing of the debt metaphor and the idea of "interest."
- Introduced briefly in Workshop 1; worth a re-read before Workshop 2 if participants want the original source.

### Martin Fowler — Technical Debt Quadrant

Link: https://martinfowler.com/bliki/TechnicalDebtQuadrant.html

Why use it:

- Helps participants think beyond simplistic "good vs. bad" design decisions.
- Useful in debrief when participants want to distinguish deliberate debt from accidental debt.

---

## How to use these during class

- Read **Code Smell** before the "Smell or Debt?" lightweight activity.
- Scan **Twelve-Factor App** before the Friction Map exercise — it helps participants spot environment, config, and release debt they would otherwise miss.
- Keep **Principles of Technical Documentation** as a reference for anyone whose debt inventory is heavy on knowledge-debt items.

---

## Cheat-sheet framing

- A **code smell** is a local, surface-level signal. It is usually cheap to fix in isolation.
- **Technical debt** is broader — it shows up in environment, data, release, operations, security, and workflow, not just code.
- The **interest** is whatever the team keeps paying because the debt exists.
- The **principal** rarely appears on a roadmap. The interest is paid quietly, forever, until someone names it.
