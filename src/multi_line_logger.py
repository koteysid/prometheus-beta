import logging

def log_multi_line(message, level=logging.INFO, separator='=', separator_length=40):
    """
    Log a multi-line message with optional separation lines.

    Args:
        message (str): The message to be logged
        level (int, optional): Logging level. Defaults to logging.INFO
        separator (str, optional): Character used for separation lines. Defaults to '='.
        separator_length (int, optional): Length of separation lines. Defaults to 40.

    Raises:
        TypeError: If message is not a string, separator is not a single character, 
                   or separator_length is not a positive integer
        ValueError: If separator is an empty string
    """
    # Validate input types and values
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not isinstance(separator, str) or len(separator) != 1:
        raise TypeError("Separator must be a single character")
    
    if not isinstance(separator_length, int) or separator_length <= 0:
        raise TypeError("Separator length must be a positive integer")

    # Create logger
    logger = logging.getLogger(__name__)

    # Create separation line
    sep_line = separator * separator_length

    # Log the message with separation lines
    if level == logging.DEBUG:
        log_func = logger.debug
    elif level == logging.INFO:
        log_func = logger.info
    elif level == logging.WARNING:
        log_func = logger.warning
    elif level == logging.ERROR:
        log_func = logger.error
    elif level == logging.CRITICAL:
        log_func = logger.critical
    else:
        raise ValueError("Invalid logging level")

    # Log with separation lines
    log_func(sep_line)
    for line in message.splitlines():
        log_func(line)
    log_func(sep_line)