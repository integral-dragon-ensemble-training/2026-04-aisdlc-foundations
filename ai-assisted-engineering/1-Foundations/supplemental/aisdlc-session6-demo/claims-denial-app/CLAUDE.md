# Claims Denial Worklist & Analytics Dashboard

## Project Overview

This is a demo application for the AISDLC course. It demonstrates task decomposition, parallel agent execution, and orchestration pipeline concepts using a realistic RCM (Revenue Cycle Management) use case.

## Architecture

- **UI**: React SPA in `src/ui/`
- **API**: Node.js + Express REST API in `src/api/`
- **DB**: PostgreSQL with migrations in `src/db/`

## Conventions

- Use TypeScript for all layers
- Follow RESTful naming conventions for API endpoints
- All database changes go through migration scripts — no manual schema edits
- Seed data must be realistic enough to demo with (real CARC codes, plausible payer names, varied aging buckets)
- Every denial action must write to the audit trail

## Directory Structure

```
src/
  ui/          — React frontend
  api/         — Express API server
  db/
    migrations/ — Schema migration scripts (run in order)
    seeds/      — Seed data scripts
    models/     — Database models / query layer
```

## Development

- `npm install` in root to install all dependencies
- `npm run dev:api` to start the API server
- `npm run dev:ui` to start the React dev server
- `npm run db:migrate` to run migrations
- `npm run db:seed` to load seed data

## Quality Gates

- All API endpoints must have input validation
- All API endpoints must return consistent error format
- UI components must handle loading and error states
- No hardcoded credentials or connection strings in source files
