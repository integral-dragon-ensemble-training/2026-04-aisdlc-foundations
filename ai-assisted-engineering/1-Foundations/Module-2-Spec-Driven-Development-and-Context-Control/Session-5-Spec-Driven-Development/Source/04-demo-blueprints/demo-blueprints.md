# Demo Blueprints

## Session 05

## Spec-Driven Development

### Demo 01

## Weak request vs executable spec

### Goal

Show that the same model produces very different implementation quality depending on whether the input is an informal ask or a bounded specification.

### Suggested flow

1. Start with a weak request:
   `Build me a password reset endpoint.`
2. Ask Claude to outline what is underspecified.
3. Replace it with a compact markdown spec.
4. Compare the resulting implementation plan, edge-case handling, and likely testability.

### Teaching points

- bad outputs often originate from missing constraints
- ambiguity multiplies later in the workflow
- the spec reduces rework before code exists

### Demo 02

## Acceptance-criteria rewrite

### Goal

Show students how to convert soft language into observable checks.

### Suggested flow

1. Present three vague criteria on screen.
2. Ask Claude:
   `Rewrite these as binary acceptance criteria for an enterprise API change.`
3. Challenge one rewritten criterion and force a sharper version.

### Teaching points

- criteria must be reviewable
- criteria should imply tests and diff boundaries
- the review loop starts before Act Mode

### Demo 03

## Spec to task slices

### Goal

Show how a compact spec leads naturally to smaller PR slices.

### Suggested flow

1. Feed Claude the final spec.
2. Ask:
   `Break this into 2 to 3 reviewable work packets with file-level impact and risks.`
3. Inspect whether the slices preserve the spec without widening scope.

### Teaching points

- a clear spec improves decomposition quality
- smaller slices are easier to test and narrate
- this is the handoff point into Session 06
