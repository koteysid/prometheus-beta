"""
Unit tests for LZH Compression Algorithm
"""

import pytest
import random
from src.lzh_compression import (
    lzh_compress, 
    lzh_decompress, 
    build_frequency_table, 
    build_huffman_tree, 
    generate_huffman_codes,
    lzw_compress
)

def test_build_frequency_table():
    """Test frequency table generation."""
    data = b'hello world'
    freq = build_frequency_table(data)
    
    assert freq[ord('h')] == 1
    assert freq[ord('e')] == 1
    assert freq[ord('l')] == 3
    assert freq[ord('o')] == 2
    assert freq[ord(' ')] == 1
    assert freq[ord('w')] == 1
    assert freq[ord('r')] == 1
    assert freq[ord('d')] == 1

def test_huffman_tree_and_codes():
    """Test Huffman tree and code generation."""
    data = b'hello world'
    freq = build_frequency_table(data)
    tree = build_huffman_tree(freq)
    codes = generate_huffman_codes(tree)
    
    assert isinstance(codes, dict)
    assert all(isinstance(code, str) for code in codes.values())
    assert all(isinstance(char, int) for char in codes.keys())

def test_lzw_compress():
    """Test basic LZW compression."""
    data = b'TOBEORNOTTOBEORTOBEORNOT'
    compressed = lzw_compress(data)
    
    assert isinstance(compressed, list)
    assert all(isinstance(x, int) for x in compressed)
    assert len(compressed) < len(data)

def test_lzh_compress_decompress_basic():
    """Test basic LZH compression and decompression."""
    original_data = b'Hello, world! This is a test of LZH compression.'
    
    # Compress
    compressed = lzh_compress(original_data)
    assert 'compressed_data' in compressed
    assert 'huffman_codes' in compressed
    
    # Decompress
    decompressed = lzh_decompress(
        compressed['compressed_data'], 
        compressed['huffman_codes']
    )
    
    assert decompressed == original_data

def test_lzh_empty_input():
    """Test compression and decompression with empty input."""
    empty_data = b''
    
    # Compress
    compressed = lzh_compress(empty_data)
    assert compressed == {}
    
    # Decompress (effectively a no-op)
    decompressed = lzh_decompress([], {})
    assert decompressed == b''

def test_lzh_random_data():
    """Test LZH compression with random data."""
    # Generate random bytes
    random.seed(42)  # for reproducibility
    random_data = bytes(random.getrandbits(8) for _ in range(1000))
    
    # Compress
    compressed = lzh_compress(random_data)
    
    # Decompress
    decompressed = lzh_decompress(
        compressed['compressed_data'], 
        compressed['huffman_codes']
    )
    
    assert decompressed == random_data

def test_edge_cases():
    """Test various edge cases."""
    # Single character
    single_char = b'a' * 100
    compressed = lzh_compress(single_char)
    decompressed = lzh_decompress(
        compressed['compressed_data'], 
        compressed['huffman_codes']
    )
    assert decompressed == single_char
    
    # Repeated sequence
    repeated_seq = b'abc' * 50
    compressed = lzh_compress(repeated_seq)
    decompressed = lzh_decompress(
        compressed['compressed_data'], 
        compressed['huffman_codes']
    )
    assert decompressed == repeated_seq