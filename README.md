# Financial Analysis Agent

[![CI](https://github.com/kogunlowo123/financial-analysis-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/financial-analysis-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Business Intelligence | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Financial analysis agent that performs variance analysis, builds financial models, generates P&L breakdowns, calculates unit economics, and provides scenario planning for budget and forecast cycles.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_variance` | Perform budget vs actual variance analysis with root cause |
| `build_financial_model` | Build a financial model with assumptions and projections |
| `break_down_pl` | Break down P&L by department, product, or geography |
| `calculate_unit_economics` | Calculate unit economics (CAC, LTV, payback period, margins) |
| `run_scenario` | Run scenario analysis with different assumption sets |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/finance/variance` | Analyze variance |
| `POST` | `/api/v1/finance/model` | Build financial model |
| `GET` | `/api/v1/finance/pl` | Break down P&L |
| `POST` | `/api/v1/finance/unit-economics` | Calculate unit economics |
| `POST` | `/api/v1/finance/scenarios` | Run scenario analysis |

## Features

- Variance Analysis
- Financial Modeling
- Pl Breakdown
- Unit Economics
- Scenario Planning

## Integrations

- Netsuite
- Quickbooks
- Xero
- Snowflake
- Google Sheets

## Architecture

```
financial-analysis-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── financial_analysis_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Financial Data + Modeling Engine + LLM**

---

Built as part of the Enterprise AI Agent Platform.
