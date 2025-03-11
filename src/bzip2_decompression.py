import bz2
import os


def decompress_bzip2_file(compressed_file_path, output_path=None):
    """
    Decompress a bzip2-compressed file.

    Args:
        compressed_file_path (str): Path to the bzip2-compressed input file.
        output_path (str, optional): Path to save the decompressed file. 
                                     If None, uses input filename without .bz2 extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If the input compressed file does not exist.
        IsADirectoryError: If the input path is a directory.
        PermissionError: If there are insufficient permissions to read/write.
        ValueError: If the input file is not a valid bzip2 compressed file.
    """
    # Validate input file exists and is a file
    if not os.path.exists(compressed_file_path):
        raise FileNotFoundError(f"Compressed file not found: {compressed_file_path}")
    
    if os.path.isdir(compressed_file_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {compressed_file_path}")

    # Determine output path
    if output_path is None:
        # Remove .bz2 extension if present
        if compressed_file_path.endswith('.bz2'):
            output_path = compressed_file_path[:-4]
        else:
            output_path = compressed_file_path + '.decompressed'

    try:
        # Open and read compressed file
        with bz2.open(compressed_file_path, 'rb') as compressed_file:
            # Read and decompress contents
            decompressed_content = compressed_file.read()

        # Write decompressed content to output file
        with open(output_path, 'wb') as output_file:
            output_file.write(decompressed_content)

        return output_path

    except bz2.BZip2Error:
        raise ValueError(f"Invalid bzip2 compressed file: {compressed_file_path}")