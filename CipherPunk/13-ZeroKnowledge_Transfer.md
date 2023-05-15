Algorithm of zero-knowledge transfer money system:

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
