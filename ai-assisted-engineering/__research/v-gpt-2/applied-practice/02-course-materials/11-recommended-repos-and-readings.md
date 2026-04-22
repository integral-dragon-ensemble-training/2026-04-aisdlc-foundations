ChatGPT Folder > aisdlc-applied-practice > AI-SDLC Course Bundle > 11-recommended-repos-and-readings.md

# Recommended Repositories and Readings

## Claude Code CLI

### Official docs
- Claude Code overview — https://code.claude.com/docs
- Routines — https://code.claude.com/docs/en/routines
- Anthropic product overview — https://www.anthropic.com/product/claude-code
- Claude Code auto mode article — https://www.anthropic.com/engineering/claude-code-auto-mode

### How to use them in class
- Use the overview docs to ground installation, CLI launch, and core workflow claims.
- Use routines only as advanced or optional discussion material.
- Use the auto mode article to discuss approval fatigue, review discipline, and safe automation.

## Azure and Microsoft documentation

### Azure platform and deployment
- Azure developer documentation — https://learn.microsoft.com/en-us/azure/developer/
- Azure Developer CLI overview — https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/overview
- Azure CLI docs — https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest

### .NET and observability
- .NET CLI docs — https://learn.microsoft.com/en-us/dotnet/core/tools/
- .NET Aspire — https://aspire.dev/
- .NET observability with OpenTelemetry — https://learn.microsoft.com/en-us/dotnet/core/diagnostics/observability-with-otel
- Application Insights + OpenTelemetry overview — https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
- Azure Functions with OpenTelemetry — https://learn.microsoft.com/en-us/azure/azure-functions/opentelemetry-howto

### Python on Azure
- Azure developer documentation for Python — https://learn.microsoft.com/en-us/azure/developer/python/
- Azure SDK for Python overview — https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-overview

## GitHub repositories for teaching examples

### 1. dotnet/eShop
- Link — https://github.com/dotnet/eshop
- Why it is useful — reference .NET application, services-based architecture, useful for architecture clarity, tests, and observability discussion
- What to inspect — solution structure, README, project boundaries, Aspire usage, testing approach
- Caveat — larger than needed for a one-hour class; use targeted slices

### 2. dotnet/aspire-samples
- Link — https://github.com/dotnet/aspire-samples
- Why it is useful — concrete samples for distributed application patterns and observability-friendly development
- What to inspect — startup patterns, composition, telemetry assumptions
- Caveat — sample repo, not a brownfield enterprise app by itself

### 3. microsoft/aspire
- Link — https://github.com/microsoft/aspire
- Why it is useful — strong reference for modern .NET distributed app tooling, observability, and local orchestration ideas
- What to inspect — docs, app host model, service defaults, repo organization
- Caveat — more platform/tooling oriented than typical business app repos

### 4. open-telemetry/opentelemetry-demo
- Link — https://github.com/open-telemetry/opentelemetry-demo
- Why it is useful — excellent for observability teaching, especially logs/metrics/traces and request flow
- What to inspect — telemetry wiring, dashboards, multi-service flow
- Caveat — not Azure-specific; translate concepts into Azure Monitor/Application Insights

### 5. Azure-Samples/functions-quickstart-dotnet-azd
- Link — https://github.com/Azure-Samples/functions-quickstart-dotnet-azd
- Why it is useful — small Azure-oriented example for repeatable deploy/build and secure defaults
- What to inspect — azd flow, config, deployment shape, local-to-cloud expectations
- Caveat — more template-like than brownfield

### 6. Azure-Samples/functions-quickstart-python-http-azd
- Link — https://github.com/Azure-Samples/functions-quickstart-python-http-azd
- Why it is useful — Python counterpart to the Azure deploy workflow
- What to inspect — Python service shape, azd config, testing and deployment assumptions
- Caveat — narrower scope than a larger service platform

### 7. Azure/azure-sdk-for-net
- Link — https://github.com/Azure/azure-sdk-for-net
- Why it is useful — high-quality .NET repo structure and engineering discipline reference
- What to inspect — repo hygiene, contribution patterns, testing layout, standards
- Caveat — SDK repo dynamics are different from typical business applications

### 8. Azure/azure-sdk-for-python
- Link — https://github.com/Azure/azure-sdk-for-python
- Why it is useful — useful reference for Python package organization and engineering discipline
- What to inspect — package layout, tests, standards, documentation
- Caveat — library ecosystem repo, not a standard enterprise application

## Suggested mapping by course day

### Day 1
Read:
- Claude Code overview
- Azure developer documentation landing page

Inspect:
- dotnet/eShop
- Azure SDK repo structure

### Day 2
Read:
- .NET CLI docs
- Azure Developer CLI overview

Inspect:
- Azure-Samples/functions-quickstart-dotnet-azd
- Azure-Samples/functions-quickstart-python-http-azd

### Day 3
Read:
- .NET testing and observability docs as needed
- repo-specific test sections in sample repos

Inspect:
- dotnet/eShop test projects
- Azure SDK repo test structure

### Day 4
Read:
- .NET observability with OpenTelemetry
- Application Insights + OpenTelemetry overview
- Azure Functions OpenTelemetry docs if serverless is relevant

Inspect:
- opentelemetry-demo
- Aspire samples

### Day 5
Read:
- Claude Code auto mode article
- Claude Code routines docs as optional advanced reading

Inspect:
- any repo students have already scored and discussed
- focus on change planning, guardrails, and reviewability

## How to present the resource list to students

Do not dump all links at once.
Give students:
- a required list for the week
- an optional list for deeper study
- one or two repos per day to inspect
