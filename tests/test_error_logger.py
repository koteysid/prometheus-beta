import logging
import pytest
import io
import sys
from src.error_logger import log_custom_error

def test_log_custom_error_with_message():
    """Test logging a custom message without an exception."""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.DEBUG)

    # Log a custom message
    log_custom_error("Test error message")

    # Check log output
    log_output = log_capture.getvalue()
    assert "Test error message" in log_output
    assert "ERROR" in log_output

    # Clean up
    logging.getLogger().removeHandler(handler)
    log_capture.close()

def test_log_custom_error_with_exception():
    """Test logging a custom message with an exception."""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.DEBUG)

    # Simulate an exception
    try:
        raise ValueError("Sample error")
    except ValueError as e:
        log_custom_error("An error occurred", e)

    # Check log output
    log_output = log_capture.getvalue()
    assert "An error occurred" in log_output
    assert "ValueError" in log_output
    assert "Sample error" in log_output
    assert "Traceback" in log_output

    # Clean up
    logging.getLogger().removeHandler(handler)
    log_capture.close()

def test_log_custom_error_custom_log_level():
    """Test logging with a custom log level."""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.DEBUG)

    # Log with a warning level
    log_custom_error("Warning message", log_level=logging.WARNING)

    # Check log output
    log_output = log_capture.getvalue()
    assert "Warning message" in log_output
    assert "WARNING" in log_output

    # Clean up
    logging.getLogger().removeHandler(handler)
    log_capture.close()