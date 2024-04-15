"""
Calculates the CRC32C checksum of a file and returns it as a Base64-encoded string.
"""

import crc32c
import base64

def calculate_crc32c(file_path):
    """
    Calculates the CRC32C checksum of the given file.

    Args:
        file_path (str): The path to the file to checksum.

    Returns:
        str: The Base64-encoded CRC32C checksum of the file.
    """

    with open(file_path, 'rb') as file:
        """
        Opens the file in binary read mode (`'rb'`) to ensure proper handling of binary data.
        """

        file_content = file.read()
        """
        Reads the entire file content into memory for checksum calculation.
        """

        crc32c_value = crc32c.crc32c(file_content)
        """
        Calculates the CRC32C checksum of the file content using the `crc32c` module.
        """

        crc_bytes = crc32c_value.to_bytes(4, byteorder='big')
        """
        Converts the checksum integer to a 4-byte binary representation in big-endian byte order.
        """

        crc_hash = base64.b64encode(crc_bytes).decode('utf-8')
        """
        Encodes the checksum bytes as a Base64 string for easier readability and portability.
        """

    return crc_hash

# Example usage:
file_path = ""  # Replace with the actual file path
crc_value = calculate_crc32c(file_path)
print("CRC32C value from the downloaded file: ", crc_value)
