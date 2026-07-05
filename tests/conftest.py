"""Test configuration for Financial Analysis Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "financial-analysis-agent", "category": "Business Intelligence"}
