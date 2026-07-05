"""Financial Analysis Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_variance():
    """Test Perform budget vs actual variance analysis with root cause."""
    tools = AgentTools()
    result = await tools.analyze_variance(period="test", budget_data="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_build_financial_model():
    """Test Build a financial model with assumptions and projections."""
    tools = AgentTools()
    result = await tools.build_financial_model(model_type="test", assumptions="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_break_down_pl():
    """Test Break down P&L by department, product, or geography."""
    tools = AgentTools()
    result = await tools.break_down_pl(period="test", dimension="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_calculate_unit_economics():
    """Test Calculate unit economics (CAC, LTV, payback period, margins)."""
    tools = AgentTools()
    result = await tools.calculate_unit_economics(cohort="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.financial_analysis_agent_agent import FinancialAnalysisAgentAgent
    agent = FinancialAnalysisAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
