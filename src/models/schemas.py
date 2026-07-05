"""Financial Analysis Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class VarianceAnalysis(BaseModel):
    """VarianceAnalysis for Financial Analysis Agent."""
    line_item: str
    budget: float
    actual: float
    variance: float
    variance_pct: float
    root_cause: str


class UnitEconomics(BaseModel):
    """UnitEconomics for Financial Analysis Agent."""
    cac: float
    ltv: float
    ltv_cac_ratio: float
    payback_months: float
    gross_margin: float

