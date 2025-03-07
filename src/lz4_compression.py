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
    window_size = 65535
    
    i = 0
    while i < len(data):
        # Find the best match in the sliding window
        best_match_length = 0
        best_match_offset = 0
        
        # Search window
        window_start = max(0, i - window_size)
        for j in range(window_start, i):
            # Check match length
            match_length = 0
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = i - j
        
        # Encode token
        if best_match_length >= 4:
            # Match token (token | offset)
            token = min(15, best_match_length - 4) << 4 | (best_match_offset >> 8)
            offset_low = best_match_offset & 0xFF
            
            # Append token and offset
            compressed.append(token)
            compressed.append(offset_low)
            
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
        # Read token
        token = data[i]
        i += 1
        
        # Literal length
        literal_length = token >> 4
        
        # Copy literals
        if literal_length == 15:
            # Extended literal length
            while data[i] == 255:
                literal_length += 255
                i += 1
            literal_length += data[i]
            i += 1
        
        # Add literals
        if i + literal_length > len(data):
            break
        
        decompressed.extend(data[i:i+literal_length])
        i += literal_length
        
        # If end of data, break
        if i >= len(data):
            break
        
        # Match offset and length
        match_offset = data[i] | (token & 0x0F) << 8
        i += 1
        
        # Match length
        match_length = (token >> 4) + 4
        
        # Reproduce match
        for _ in range(match_length):
            if match_offset > len(decompressed):
                break
            
            repeated_byte = decompressed[-match_offset]
            decompressed.append(repeated_byte)
    
    return bytes(decompressed)