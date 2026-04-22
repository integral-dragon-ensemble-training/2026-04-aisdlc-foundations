# Product Requirement Document
## Claims Denial Worklist & Analytics Dashboard

### Background

When a health insurance payer denies a medical claim, a revenue cycle specialist must investigate the denial, determine the appropriate corrective action, and either appeal the denial or correct and resubmit the claim. This process is currently managed through a combination of disconnected queue systems, spreadsheets, and manual tracking. Denials that age past filing deadlines become unrecoverable revenue.

### Product Vision

Build a web application that gives denial management teams a single view of their denied claims, automates categorization by denial reason, supports worklist-based task assignment, and provides analytics to surface denial trends by payer, reason code, and aging bucket.

### Users

- **Denial Specialists** — work individual denials from a queue, research root cause, take corrective action (appeal, resubmit, write-off)
- **Team Leads** — assign work, monitor queue depth and aging, redistribute load
- **Managers** — view dashboard analytics for denial trends, recovery rates, and team performance

---

## Functional Requirements

### Worklist

- Display denied claims in a filterable, sortable worklist
- Filter by: payer, denial reason code (CARC/RARC), aging bucket (0-30, 31-60, 61-90, 90+), assigned specialist, dollar amount range, facility
- Allow a specialist to claim a denial from the queue
- Show denial detail view: patient info, payer, claim number, billed amount, denial reason code and description, date of service, filing deadline, prior actions taken
- Support actions on a denial: appeal, correct and resubmit, write-off with reason, add note, reassign
- Track action history as an audit trail on each denial

### Denial Categorization

- Auto-categorize incoming denials by CARC (Claim Adjustment Reason Code) and RARC (Remittance Advice Remark Code)
- Group reason codes into denial categories: eligibility, authorization, coding, timely filing, medical necessity, duplicate, bundling, other
- Suggest likely next action based on denial category and payer-specific historical success rates
- Flag denials approaching filing deadline (within 15 days)

### Analytics Dashboard

- Total denied dollars by period (weekly, monthly, quarterly)
- Denial volume and dollar amount by reason category (stacked bar)
- Top 10 denial reason codes by frequency and dollar impact
- Aging distribution of open denials
- Recovery rate: percentage of denied dollars successfully recovered via appeal or resubmission
- Average days to resolution by denial category
- Payer comparison: denial rate and recovery rate by payer
- Specialist productivity: denials worked, resolved, and recovery rate per user

### Assignment and Workflow

- Auto-assign new denials to specialists based on configurable rules (round-robin, payer specialty, denial category)
- Allow team leads to manually reassign denials
- Support priority escalation for high-dollar denials (configurable threshold, default $10,000)
- Email or in-app notification when a denial is assigned or approaching deadline

---

## Technical Requirements

### UI Layer

- React single-page application
- Responsive layout (desktop primary, tablet secondary)
- Worklist table with virtual scrolling for large result sets
- Dashboard charts using a charting library (Recharts or similar)
- Role-based navigation: specialists see worklist, leads see worklist + assignment tools, managers see dashboard + worklist

### API Layer

- RESTful API built with Node.js and Express
- Endpoints:
  - `GET /api/denials` — search and filter denials
  - `GET /api/denials/:id` — denial detail with action history
  - `POST /api/denials/:id/actions` — record an action (appeal, resubmit, write-off, note)
  - `PUT /api/denials/:id/assign` — assign or reassign a denial
  - `GET /api/analytics/summary` — dashboard summary metrics
  - `GET /api/analytics/trends` — time-series denial trends
  - `GET /api/analytics/payers` — payer comparison data
  - `GET /api/reason-codes` — list CARC/RARC codes with categories
  - `POST /api/denials/import` — bulk import denials from a file
- Input validation on all endpoints
- Error responses follow a consistent format with appropriate HTTP status codes
- Authentication via JWT tokens (stub implementation acceptable for demo)

### Database Layer

- PostgreSQL relational database
- Core tables:
  - `claims` — original claim data (claim_number, patient_id, payer_id, facility, billed_amount, date_of_service)
  - `denials` — denial record linked to claim (denial_date, carc_code, rarc_code, category, status, assigned_to, priority, filing_deadline)
  - `denial_actions` — audit trail (denial_id, action_type, performed_by, timestamp, notes, outcome)
  - `payers` — payer reference data (name, filing_deadline_days, appeal_address)
  - `reason_codes` — CARC/RARC reference (code, description, category, suggested_action)
  - `users` — application users (name, role, email, active)
  - `analytics_summary` — materialized rollup for dashboard performance (refreshed on schedule)
- Seed data:
  - 10 payers with realistic names and filing deadlines
  - 50 CARC/RARC codes with categories and suggested actions
  - 500 sample denied claims spread across payers, reason codes, and aging buckets
  - 5 users (2 specialists, 1 lead, 1 manager, 1 admin)
- Migration scripts for schema creation and seed data loading

---

## Non-Functional Requirements

- API response time under 500ms for worklist queries
- Dashboard should render within 2 seconds on initial load
- All denial actions must be persisted to the audit trail — no silent failures
- Role-based access control enforced at the API layer, not just the UI

---

## Out of Scope for Initial Build

- Real payer integration or EDI connectivity
- Production authentication provider (OAuth, SSO)
- Real-time claim status updates from clearinghouses
- Mobile-native application
- PDF generation for appeal letters (future enhancement)

---

## Success Criteria

- A specialist can log in, view their assigned denials, filter by payer and aging, open a denial, and submit an appeal action — all in under 60 seconds
- A manager can open the dashboard and see denial trends by payer and reason code with data from the seed set
- All actions are captured in the audit trail and visible in the denial detail view
