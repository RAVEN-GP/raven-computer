import sys
import os
import pytest

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_dashboard_files_exist():
    """Test that the dashboard app file exists."""
    assert os.path.exists("src/dashboard/app.py")

def test_requirements_exist():
    """Test that requirements.txt exists."""
    assert os.path.exists("requirements.txt")
