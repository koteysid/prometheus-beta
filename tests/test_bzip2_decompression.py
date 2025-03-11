import os
import bz2
import pytest
from src.bzip2_decompression import decompress_bzip2_file


@pytest.fixture
def sample_bzip2_file(tmp_path):
    """Create a sample bzip2 compressed file for testing."""
    content = b"This is a test file for bzip2 decompression."
    compressed_file = tmp_path / "sample.txt.bz2"
    
    with bz2.open(compressed_file, 'wb') as f:
        f.write(content)
    
    return compressed_file


def test_successful_decompression(sample_bzip2_file, tmp_path):
    """Test successful decompression of a bzip2 file."""
    output_path = tmp_path / "decompressed.txt"
    
    # Decompress the file
    result_path = decompress_bzip2_file(str(sample_bzip2_file), str(output_path))
    
    # Verify the file was created and contains correct content
    assert os.path.exists(result_path)
    with open(result_path, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."


def test_default_output_path(sample_bzip2_file, tmp_path):
    """Test decompression with default output path."""
    # Decompress without specifying output path
    result_path = decompress_bzip2_file(str(sample_bzip2_file))
    
    # Verify the file was created with expected filename
    expected_path = str(sample_bzip2_file)[:-4]  # Remove .bz2 extension
    assert result_path == expected_path
    assert os.path.exists(result_path)


def test_nonexistent_file():
    """Test decompression of a non-existent file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("/path/to/nonexistent/file.bz2")


def test_directory_input(tmp_path):
    """Test attempting to decompress a directory."""
    with pytest.raises(IsADirectoryError):
        decompress_bzip2_file(str(tmp_path))


def test_invalid_bzip2_file(tmp_path):
    """Test decompression of an invalid bzip2 file."""
    invalid_file = tmp_path / "invalid.bz2"
    
    # Create an invalid bzip2 file by writing random bytes
    with open(invalid_file, 'wb') as f:
        f.write(b"This is not a valid bzip2 file")
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(str(invalid_file))