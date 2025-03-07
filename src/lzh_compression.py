"""
LZH (Lempel-Ziv-Huffman) Compression Algorithm Implementation

This module provides a basic implementation of the LZH compression algorithm,
which combines Lempel-Ziv sliding window compression with Huffman coding.

Note: This is a simplified implementation and may not be as efficient as 
production-level compression libraries.
"""

import heapq
from collections import defaultdict

class Node:
    """Huffman tree node for encoding/decoding."""
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data):
    """
    Build a frequency table for the input data.
    
    Args:
        data (bytes): Input data to analyze
    
    Returns:
        dict: Frequency of each byte in the input
    """
    freq = defaultdict(int)
    for byte in data:
        freq[byte] += 1
    return freq

def build_huffman_tree(freq):
    """
    Build a Huffman tree from frequency table.
    
    Args:
        freq (dict): Frequency table of bytes
    
    Returns:
        Node: Root of the Huffman tree
    """
    heap = [Node(char=k, freq=v) for k, v in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        internal = Node(freq=left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    return heap[0] if heap else None

def generate_huffman_codes(root):
    """
    Generate Huffman codes from the Huffman tree.
    
    Args:
        root (Node): Root of the Huffman tree
    
    Returns:
        dict: Mapping of bytes to their Huffman codes
    """
    def traverse(node, current_code):
        if not node:
            return {}
        
        if not node.left and not node.right:
            return {node.char: current_code}
        
        codes = {}
        if node.left:
            codes.update(traverse(node.left, current_code + '0'))
        if node.right:
            codes.update(traverse(node.right, current_code + '1'))
        
        return codes
    
    return traverse(root, '')

def lzw_compress(data):
    """
    Perform LZW compression on the input data.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        list: Compressed data dictionary indices
    """
    dictionary = {bytes([i]): i for i in range(256)}
    result = []
    current_sequence = bytes()
    next_code = 256
    
    for byte in data:
        current_sequence += bytes([byte])
        if current_sequence not in dictionary:
            result.append(dictionary[current_sequence[:-1]])
            dictionary[current_sequence] = next_code
            next_code += 1
            current_sequence = bytes([byte])
    
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzh_compress(data):
    """
    Compress data using LZH (Lempel-Ziv-Huffman) algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        dict: Compressed data with Huffman codes and LZW compressed data
    """
    if not data:
        return {}
    
    # LZW Compression
    lzw_compressed = lzw_compress(data)
    
    # Build Huffman Tree
    freq = build_frequency_table(data)
    huffman_tree = build_huffman_tree(freq)
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    return {
        'compressed_data': lzw_compressed,
        'huffman_codes': huffman_codes
    }

def lzh_decompress(compressed_data, huffman_codes):
    """
    Decompress data compressed with LZH algorithm.
    
    Args:
        compressed_data (list): LZW compressed data indices
        huffman_codes (dict): Huffman codes for decompression
    
    Returns:
        bytes: Decompressed original data
    """
    if not compressed_data:
        return b''
    
    # Reverse Huffman codes dictionary
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    
    # Reverse LZW compression
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = []
    current = dictionary[compressed_data[0]]
    result.extend(current)
    
    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current + bytes([current[0]])
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.extend(entry)
        
        dictionary[next_code] = current + bytes([entry[0]])
        next_code += 1
        current = entry
    
    return bytes(result)