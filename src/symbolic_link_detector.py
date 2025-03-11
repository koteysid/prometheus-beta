import os

def is_symbolic_link(file_path):
    """
    Detect whether the given file path is a symbolic link.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is a symbolic link, False otherwise.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the file path is empty or None.
        FileNotFoundError: If the file does not exist.
    """
    # Check for invalid input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check for empty or whitespace-only string
    if not file_path or file_path.isspace():
        raise ValueError("File path cannot be empty or whitespace")
    
    # Normalize the path to handle potential relative paths
    normalized_path = os.path.normpath(file_path)
    
    # Check if the file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"No file found at path: {normalized_path}")
    
    # Use os.path.islink() to check if it's a symbolic link
    return os.path.islink(normalized_path)