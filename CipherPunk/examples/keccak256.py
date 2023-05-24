import hashlib

def keccak256(data):
    # Pre-processing: padding the data with the appropriate number of zeros
    block_size = 136
    zero_padding = block_size - len(data) % block_size - 1
    padded_data = data + b'\x00' * zero_padding + b'\x01'

    # Computing the Keccak-256 hash
    keccak = hashlib.sha3_256()
    keccak.update(padded_data)
    return keccak.digest()


# ----------------------------------------
# Define a message to hash
message = b'Hello, world!'

# Compute the Keccak-256 hash of the message using our function
hash = keccak256(message)

# Print the hash in hexadecimal format
print(hash.hex())

