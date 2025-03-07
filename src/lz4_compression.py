"""
LZ4 Compression Algorithm Implementation

This module provides a basic implementation of the LZ4 compression algorithm.
Note: This is a simplified version and not a full production-ready LZ4 implementation.
"""

def lz4_compress(data):
    """
    Compress input data using a simplified LZ4 compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Look for matches in a sliding window
        best_match_length = 0
        best_match_offset = 0
        window_start = max(0, i - 65535)
        
        for j in range(window_start, i):
            match_length = 0
            
            # Verify sequential match
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match if longer
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = i - j
        
        # Decide whether to encode a match or literal
        if best_match_length >= 4:
            # Match token with length and offset
            token = (best_match_length - 4) << 4 | (best_match_offset >> 8)
            compressed.append(token)
            compressed.append(best_match_offset & 0xFF)
            i += best_match_length
        else:
            # Literal token
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lz4_decompress(data):
    """
    Decompress LZ4 compressed data.
    
    Args:
        data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or compressed data is invalid
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    decompressed = bytearray()
    i = 0
    
    while i < len(data):
        # Prevent index out of range
        if i >= len(data):
            break
        
        # Read token
        token = data[i]
        i += 1
        
        # Literal length
        literal_length = token >> 4
        
        # Extended literal length
        if literal_length == 15:
            while i < len(data) and data[i] == 255:
                literal_length += 255
                i += 1
            
            if i < len(data):
                literal_length += data[i]
                i += 1
        
        # Copy literals safely
        literal_copy_len = min(literal_length, len(data) - i)
        decompressed.extend(data[i:i+literal_copy_len])
        i += literal_copy_len
        
        # Check end of data
        if i >= len(data):
            break
        
        # Match offset
        match_offset = data[i] | (token & 0x0F) << 8
        i += 1
        
        # Match length
        match_length = (token >> 4) + 4
        
        # Reproduce match
        for _ in range(match_length):
            # Protect against invalid offsets
            if match_offset > len(decompressed):
                break
            
            repeated_byte = decompressed[-match_offset]
            decompressed.append(repeated_byte)
    
    return bytes(decompressed)