"""
tests/test_health.py — Production Unit & Health Check Suite for MPLADS-AI
"""
import sys
import os

# Ensure backend root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.endpoints.health import router

app = FastAPI(title="MPLADS-AI CI Suite")
app.include_router(router, prefix="/api/v1")

client = TestClient(app)

def test_system_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert "active_models" in data
    assert len(data["active_models"]) == 3
