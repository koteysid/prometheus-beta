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
    
    # Compression variables
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Find longest match
        best_match_length = 0
        best_match_offset = 0
        
        # Look back in data for matches
        window_start = max(0, i - 65535)
        for j in range(window_start, i):
            match_length = 0
            
            # Determine match length
            while (i + match_length < len(data) and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = i - j
        
        # Encode match or literal
        if best_match_length >= 4:
            # Encode match token
            token = best_match_length << 4
            compressed.append(token | (best_match_offset >> 8))
            compressed.append(best_match_offset & 0xFF)
            i += best_match_length
        else:
            # Encode literal
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
    
    # Decompression variables
    decompressed = bytearray()
    i = 0
    
    while i < len(data):
        # Read token
        if i >= len(data):
            break
        
        token = data[i]
        i += 1
        
        # Literals length
        literal_length = token >> 4
        
        # Copy literals
        if literal_length > 0:
            if i + literal_length > len(data):
                raise ValueError("Invalid compressed data: literal length exceeds data")
            
            decompressed.extend(data[i:i+literal_length])
            i += literal_length
        
        # Check if we've reached end of data
        if i >= len(data):
            break
        
        # Match offset
        match_offset = data[i] | (token & 0x0F) << 8
        i += 1
        
        # Match length
        match_length = token >> 4 + 4
        
        # Reproduce match
        for _ in range(match_length):
            try:
                # If match point is 0, this is OK for LZ4 algorithm
                repeated_byte = decompressed[-match_offset]
                decompressed.append(repeated_byte)
            except IndexError:
                # If we can't find match, stop decompression to avoid data corruption
                break
    
    return bytes(decompressed)