def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while gcd(e, phi) != 1:
        e += 1

    # Compute d such that d is the modular multiplicative inverse of e (mod phi)
    d = modinv(e, phi)

    return ((e, n), (d, n))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def modinv(a, m):
    # Compute the modular multiplicative inverse of a (mod m) using the extended Euclidean algorithm
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def encrypt(pk, plaintext):
    e, n = pk
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(sk, ciphertext):
    d, n = sk
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 17
    q = 19
    public, private = generate_keypair(p, q)
    message = "Hello, World!"
    encrypted_message = encrypt(public, message)
    decrypted_message = decrypt(private, encrypted_message)
    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)