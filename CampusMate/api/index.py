"""Vercel entry point for the CampusMate Flask application."""
import os
import sys

# Make the project root importable when Vercel executes this file from /api.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import app  # noqa: E402

# Vercel discovers the Flask WSGI application through this variable.
