"""
Test suite for LZ4 Compression Algorithm
"""

import pytest
import random
import string
from src.lz4_compression import lz4_compress, lz4_decompress

def generate_random_string(length):
    """Generate a random string of specified length."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def test_basic_compression_decompression():
    """Test basic string compression and decompression."""
    original = "Hello, world! This is a test of LZ4 compression."
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_repeated_data_compression():
    """Test compression of data with repetitions."""
    original = "AAAABBBBCCCCDDDD" * 10
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_large_random_data():
    """Test compression of large random data."""
    original = generate_random_string(10000)
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError):
        lz4_compress("")
    with pytest.raises(ValueError):
        lz4_decompress(b"")

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        lz4_compress(123)
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_byte_input():
    """Test compression and decompression with byte input."""
    original = b"Binary data test with some bytes"
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed == original

def test_multiple_sequential_compressions():
    """Test multiple sequential compressions."""
    data_sets = [
        "First test string",
        "Second test string with some repetition",
        generate_random_string(1000)
    ]
    
    for original in data_sets:
        compressed = lz4_compress(original)
        decompressed = lz4_decompress(compressed)
        assert decompressed.decode('utf-8') == original