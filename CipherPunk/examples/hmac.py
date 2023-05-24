def hmac(key, message, hash_func):
    block_size = 64  # bytes
    if len(key) > block_size:
        key = hash_func(key)
    key = key.ljust(block_size, b'\0')
    o_key_pad = bytes([x ^ 0x5c for x in key])
    i_key_pad = bytes([x ^ 0x36 for x in key])
    inner_result = hash_func(i_key_pad + message).digest()
    outer_result = hash_func(o_key_pad + inner_result).digest()
    return outer_result

# ==============================

import hashlib

key = b'secret_key'
message = b'This is a message'
hash_func = hashlib.sha256

hmac_result = hmac(key, message, hash_func)
print(hmac_result.hex())