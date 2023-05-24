import hashlib

def kdf(key, salt, length):
    # Concatenate the key and salt
    data = key + salt

    # Repeatedly hash the data until the desired length is reached
    while len(data) < length:
        data += hashlib.sha256(data).digest()

    # Truncate the data to the desired length
    return data[:length]

if __name__ == '__main__':
    key = b'secretkey'
    salt = b'saltvalue'
    length = 16
    derived_key = kdf(key, salt, length)
    print(derived_key.hex())