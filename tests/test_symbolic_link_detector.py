import os
import pytest
import tempfile
import pathlib

from src.symbolic_link_detector import is_symbolic_link

def test_is_symbolic_link_with_symlink():
    """Test detection of a symbolic link."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a regular file
        real_file = os.path.join(tmpdir, 'real_file.txt')
        with open(real_file, 'w') as f:
            f.write('test content')
        
        # Create a symbolic link
        symlink_path = os.path.join(tmpdir, 'symlink')
        os.symlink(real_file, symlink_path)
        
        # Check that the function correctly identifies the symlink
        assert is_symbolic_link(symlink_path) is True

def test_is_symbolic_link_with_regular_file():
    """Test that a regular file is not detected as a symlink."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a regular file
        regular_file = os.path.join(tmpdir, 'regular_file.txt')
        with open(regular_file, 'w') as f:
            f.write('test content')
        
        # Check that the function returns False
        assert is_symbolic_link(regular_file) is False

def test_is_symbolic_link_with_nonexistent_file():
    """Test that a nonexistent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError):
            is_symbolic_link(nonexistent_file)

def test_is_symbolic_link_invalid_input_types():
    """Test various invalid input types."""
    # Test non-string input
    with pytest.raises(TypeError):
        is_symbolic_link(123)
    
    with pytest.raises(TypeError):
        is_symbolic_link(None)

def test_is_symbolic_link_empty_string():
    """Test empty string input."""
    with pytest.raises(ValueError):
        is_symbolic_link("")
    
    with pytest.raises(ValueError):
        is_symbolic_link(" ")