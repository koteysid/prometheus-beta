import logging
import pytest
import sys
from io import StringIO
from src.multi_line_logger import log_multi_line

def test_log_multi_line_default():
    """Test multi-line logging with default parameters"""
    # Capture log output
    log_capture = StringIO()
    root_logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    try:
        # Log a multi-line message
        message = "First line\nSecond line\nThird line"
        log_multi_line(message)

        # Get log output
        log_output = log_capture.getvalue()

        # Check log output
        assert '=' * 40 in log_output
        assert 'First line' in log_output
        assert 'Second line' in log_output
        assert 'Third line' in log_output
    finally:
        # Clean up the handler
        root_logger.removeHandler(handler)

def test_log_multi_line_custom_separator():
    """Test multi-line logging with custom separator"""
    log_capture = StringIO()
    root_logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    try:
        message = "Custom separator test"
        log_multi_line(message, separator='*', separator_length=20)

        log_output = log_capture.getvalue()

        assert '*' * 20 in log_output
        assert 'Custom separator test' in log_output
    finally:
        root_logger.removeHandler(handler)

def test_log_multi_line_different_levels():
    """Test logging at different levels"""
    # Test each log level
    levels = [
        (logging.DEBUG, 'debug'),
        (logging.INFO, 'info'),
        (logging.WARNING, 'warning'),
        (logging.ERROR, 'error'),
        (logging.CRITICAL, 'critical')
    ]

    for level, level_name in levels:
        log_capture = StringIO()
        root_logger = logging.getLogger()
        handler = logging.StreamHandler(log_capture)
        root_logger.addHandler(handler)
        root_logger.setLevel(level)

        try:
            message = f"Test {level_name} level"
            log_multi_line(message, level=level)

            log_output = log_capture.getvalue()
            assert message in log_output
        finally:
            root_logger.removeHandler(handler)

def test_log_multi_line_error_handling():
    """Test input validation"""
    # Test non-string message
    with pytest.raises(TypeError, match="Message must be a string"):
        log_multi_line(123)

    # Test invalid separator
    with pytest.raises(TypeError, match="Separator must be a single character"):
        log_multi_line("Test", separator="too long")

    # Test invalid separator length
    with pytest.raises(TypeError, match="Separator length must be a positive integer"):
        log_multi_line("Test", separator_length=-1)

    # Test invalid logging level
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_multi_line("Test", level=999)