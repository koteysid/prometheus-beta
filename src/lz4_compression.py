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
        # Find repeated sequences
        max_match_length = 0
        max_match_offset = 0
        
        # Search window (up to 65535 bytes back)
        for j in range(max(0, i - 65535), i):
            # Check match length
            match_length = 0
            while (i + match_length < len(data) and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match
            if match_length > max_match_length:
                max_match_length = match_length
                max_match_offset = i - j
        
        # Encode match or literal
        if max_match_length >= 4:
            # Encode a match
            token = (max_match_length << 4) | (max_match_offset >> 8)
            compressed.append(token)
            compressed.append(max_match_offset & 0xFF)
            i += max_match_length
        else:
            # Encode a literal
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
        
        # Literal length
        literal_length = token >> 4
        if literal_length == 15:
            # Extended literal length
            while i < len(data) and data[i] == 255:
                literal_length += 255
                i += 1
            
            if i < len(data):
                literal_length += data[i]
                i += 1
        
        # Copy literals
        if literal_length > 0:
            if i + literal_length > len(data):
                raise ValueError("Invalid compressed data: literal length exceeds data")
            
            decompressed.extend(data[i:i+literal_length])
            i += literal_length
        
        # Check if we've reached the end of data
        if i >= len(data):
            break
        
        # Match offset
        if i >= len(data):
            break
        
        match_offset = data[i] | (token & 0x0F) << 8
        i += 1
        
        # Match length
        match_length = token >> 4
        if match_length == 15:
            # Extended match length
            while i < len(data) and data[i] == 255:
                match_length += 255
                i += 1
            
            if i < len(data):
                match_length += data[i]
                i += 1
        
        match_length += 4
        
        # Reproduce match safely
        if match_offset > len(decompressed):
            raise ValueError("Invalid compressed data: match offset out of range")
        
        for _ in range(match_length):
            repeated_byte = decompressed[-match_offset]
            decompressed.append(repeated_byte)
    
    return bytes(decompressed)