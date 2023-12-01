import requests
import lzma
import shutil

def download_file(url):
    response = requests.get(url)
    return response.content

def compress_file(data, output_filename):
    with lzma.open(output_filename, 'wb') as f_out:
        f_out.write(data)

def decompress_file(input_filename, output_filename):
    with lzma.open(input_filename, 'rb') as f_in:
        with open(output_filename, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

# Example usage:
file_url = 'https://rauterberg.employee.id.tue.nl/lecturenotes/DDM110%20CAS/Orwell-1949%201984.pdf'
compressed_file = 'compressed_file.xz'
decompressed_file = 'decompressed_file.pdf'

# Download the file from the URL
file_data = download_file(file_url)

# Compressing the file data using lzma
compress_file(file_data, compressed_file)

# Decompressing the compressed file data
decompress_file(compressed_file, decompressed_file)

# Print the sizes of original and compressed data
original_size = len(file_data)
compressed_size = len(open(compressed_file, 'rb').read())

print(f"Original Size: {original_size} bytes")
print(f"Compressed Size: {compressed_size} bytes")

# Save the original, compressed, and decompressed files
with open('original_file.pdf', 'wb') as original_file:
    original_file.write(file_data)

print(f"\nOriginal file saved to 'original_file.pdf'")
print(f"Compressed file saved to '{compressed_file}'")
print(f"Decompressed file saved to '{decompressed_file}'")
