"""
Entry point for the HDHI backend API.

Run with: uvicorn backend.main:app --reload
"""

from backend.ingestion.api import app

__all__ = ["app"]
