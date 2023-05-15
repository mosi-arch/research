List: 
- [Transfer](https://github.com/mosi-arch/research/blob/main/CipherPunk/13-ZeroKnowledge_Transfer.md#algorithm-of-zero-knowledge-transfer-money-system)
- [El-Gamal](https://github.com/mosi-arch/research/blob/main/CipherPunk/13-ZeroKnowledge_Transfer.md#algorithm-for-a-zero-knowledge-data-transfer-system-using-the-elgamal-encryption-scheme)

#

### Algorithm of zero-knowledge transfer money system:

1. Define the parameters:
   - `p`: a large prime number
   - `g`: a primitive root modulo `p`
   - `a`: the sender's private key
   - `b`: the recipient's private key
   - `A`: the sender's public key (`A = g^a mod p`)
   - `B`: the recipient's public key (`B = g^b mod p`)
   - `m`: the amount of money to be transferred

2. Sender generates a random number k and computes:
   - `r = g^k mod p`
   - `s = (B^k * m) mod p`

3. Sender sends `r` and `s` to the recipient.

4. Recipient verifies the proof as follows:
   - Check that `r` is a valid element of the group (`1 <= r <= p-1`)
   - Compute `t = (r^a * A^s) mod p`
   - Verify that `t = g^m mod p`

5. If the proof is valid, the recipient accepts the transfer and updates their balance. Otherwise, the transfer is rejected.

- Python code of this algorithm:

```python
import random

def generate_keys(p, g):
    a = random.randint(1, p-1)
    A = pow(g, a, p)
    return a, A

def transfer_money(p, g, a, A, b, B, m):
    k = random.randint(1, p-1)
    r = pow(g, k, p)
    s = (pow(B, k, p) * m) % p

    t = (pow(r, a, p) * pow(A, s, p)) % p
    if t == pow(g, m, p):
        # Accept the transfer and update balance
        return True
    else:
        # Reject the transfer
        return False

# Example usage
p = 982451653 # large prime number
g = 2 # primitive root modulo p
a, A = generate_keys(p, g)
b, B = generate_keys(p, g)

# Transfer 100 units from A to B
m = 100
xyz = transfer_money(p, g, a, A, b, B, m)
transfer_money(p, g, a, A, b, B, m)
print(xyz, m, a, A, b, B) # false = transact process
```

example output:
```js
process level: False [because xyz before transact, but transaction after that happend]
value: 100 
from: 377463712 | 609754778
to: 744736405 | 236349327
```

---

### Algorithm for a zero-knowledge data transfer system using the **ElGamal encryption scheme**:
Usecase (example): send medical history to second dr without reveal data.

1. Generate a private key and public key for the sender using the ElGamal encryption scheme. The private key consists of a random integer `x` such that `1 < x < p-1`, where `p` is a large prime number, and the public key consists of a generator g and the value `h = g^x mod p`.
  
   The sender should keep the private key secret and share the public key with the recipient.

2. The sender encrypts the data using the recipient's public key. The ElGamal encryption scheme works as follows:

   a. Choose a random integer k such that `1 < k < p-1`.
   
   b. Compute the value `c1 = g^k mod p` and `c2 = m * h^k mod p`, where m is the data to be encrypted.
   
   c. The encrypted data consists of the pair (`c1, c2`).
   
3. The sender sends the encrypted data to the recipient.

4. The recipient decrypts the data using their private key. The **ElGamal decryption scheme** works as follows:

   a. Compute the `value s = c1^x mod p`.
   
   b. Compute the value `m = c2 * s^(p-2) mod p`, where `p-2` is the modular inverse of `(p-2) mod p`.
   
   c. The decrypted data is the value `m`.
   
5. The recipient sends the decrypted data back to the sender.

6. The sender verifies that the decrypted data received from the recipient is the same as the original data that was encrypted.

- Python code of this algorithm:

```python
import random

def generate_key(p, g):
    # Generate a private key x
    x = random.randint(2, p-2)
    # Compute the public key h = g^x mod p
    h = pow(g, x, p)
    return (x, h)

def encrypt_data(m, h, g, p):
    # Choose a random integer k
    k = random.randint(2, p-2)
    # Compute c1 = g^k mod p and c2 = m * h^k mod p
    c1 = pow(g, k, p)
    c2 = (m * pow(h, k, p)) % p
    return (c1, c2)

def decrypt_data(c1, c2, x, p):
    # Compute s = c1^x mod p
    s = pow(c1, x, p)
    # Compute m = c2 * s^(p-2) mod p
    m = (c2 * pow(s, p-2, p)) % p
    return m

# Example usage
p = 1021
g = 2
# Generate sender's keys
sender_private_key, sender_public_key = generate_key(p, g)
# Generate recipient's keys (in practice, the recipient would generate their own keys)
recipient_private_key, recipient_public_key = generate_key(p, g)
# Encrypt the data using recipient's public key
m = 42
c1, c2 = encrypt_data(m, recipient_public_key, g, p)
# Decrypt the data using recipient's private key
decrypted_data = decrypt_data(c1, c2, recipient_private_key, p)
# Verify that the decrypted data is the same as the original data
assert decrypted_data == m
# Send the decrypted data back to the sender
# In practice, this step would involve sending the decrypted data over a secure channel
sender_received_data = decrypted_data

print(f'sender_received_data: {sender_received_data}\n decrypted_data: {decrypted_data}\n m: {m}, p: {p}, g: {g},\n pub1: {sender_public_key}, pub2: {recipient_public_key}')
```

output example: 

```js
sender_received_data: 42,
decrypted_data: 42,
m: 42, 
p: 1021, 
g: 2,
pub1: 389, 
pub2: 895
```
