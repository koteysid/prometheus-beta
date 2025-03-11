import logging
import traceback
from typing import Optional, Any

def log_custom_error(message: str, 
                     error: Optional[Exception] = None, 
                     log_level: int = logging.ERROR) -> None:
    """
    Log a custom error message with optional additional error details.

    Args:
        message (str): Custom error message to log
        error (Optional[Exception], optional): The exception that occurred. Defaults to None.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.

    Example:
        >>> try:
        ...     # Some code that might raise an exception
        ...     raise ValueError("Sample error")
        ... except Exception as e:
        ...     log_custom_error("An error occurred in processing", e)
    """
    # Configure basic logging if not already configured
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Log the custom message
    logging.log(log_level, message)

    # If an error is provided, log its details
    if error is not None:
        logging.log(log_level, f"Error Type: {type(error).__name__}")
        logging.log(log_level, f"Error Details: {str(error)}")
        logging.log(log_level, f"Traceback:\n{traceback.format_exc()}")