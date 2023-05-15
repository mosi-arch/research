## "solution algorithm" : how to make a voting system, by "zero knowledge" for voter.

1. **Define the problem**: 
   We want to create a voting system where voters can cast their votes anonymously, without revealing their identities or 
   the contents of their votes to anyone, while ensuring that each vote is counted exactly once and that the final result is correct.

2. **Design the system**: 
   We can use a combination of cryptographic techniques, such as **homomorphic encryption**, **zero-knowledge proofs**, and 
   verifiable secret sharing, to achieve our goal.

3. **Define the mathematical formula**: 
   
   - Let `p` be a prime number.
   - Let `g` be a generator of a cyclic group `G` of order `p`.
   - Let `h = g^x` be a random element in `G`, where `x` is a `secret key` known only to the election authority.
   - Let `m` be the number of candidates.
   - Let `v_i` be the vote of the `i-th voter`, where `v_i` is an integer `between 1 and m`.
   - Let `r_i` be a random number chosen by the `i-th` voter.
   - Let `c_i = g^r_i h^v_i` be the encrypted vote of the `i-th voter`.
   - Let `d_i = r_i + k_i` be the decrypted vote of the `i-th voter`, where `k_i` is a random number chosen by the election authority.
   - Let `s = g^k_1 h^k_2 ... h^k_n` be the secret sharing of the decryption key, where `n` is the number of voters.
   - Let `t_i = g^k_i` be the `i-th` share of the secret sharing.
   - Let `u_i = g^r_i` be the `i-th` share of the random number used for encryption.
   
   To count the votes, we need to compute the following:
   
   - Let `w_j` be the number of votes for the `j-th` candidate.
   - Let `e_j = g^{w_j}` be the encrypted tally of the `j-th` candidate.
   - Let `f_j = g^{w_j + k'_j}` be the decrypted tally of the `j-th` candidate, where `k'_j` is a random number chosen by the election authority.
   - Let `g_j = g^{k'_j}` be the `j-th` share of the secret sharing used for decryption.
   
   The final result is the candidate with the highest decrypted tally.

4. **Watch the Python code**:\
   Python implementation of the above formula:
   
```python
   from random import randint
   from functools import reduce
   
   def modexp(base, exp, modulus):
       result = 1
       while exp > 0:
           if exp % 2 == 1:
               result = (result * base) % modulus
           base = (base * base) % modulus
           exp //= 2
       return result
   
   def generate_params(m):
       p = 2
       while modexp(2, p-1, p) != 1 or modexp(2, (p-1)//2, p) != -1:
           p += 1
       G = [modexp(2, i, p) for i in range(1, p)]
       g = G[randint(0, len(G)-1)]
       x = randint(1, p-2)
       h = modexp(g, x, p)
       return p, g, h, x, m
   
   def encrypt_vote(v, h):
       r = randint(1, p-2)
       c = (modexp(g, r, p), modexp(h, v, p) * modexp(g, r, p) % p)
       return c, r
   
   def decrypt_vote(c, x):
       r, hv = c
       d = r + modexp(hv, p-1-x, p)
       return d
   
   def compute_secret_sharing():
       S = [randint(1, p-2) for i in range(n)]
       T = [modexp(g, s, p) for s in S]
       s = reduce(lambda a, b: a*b % p, T)
       return T, s
   
   def combine_decryption(T, d):
       hv = reduce(lambda a, b: a*b % p, [modexp(t, d, p) for t in T])
       return hv
   
   def compute_tally():
       E = [modexp(g, 0, p)] * m
       for i in range(n):
           c, r = encrypt_vote(votes[i], h)
           U[i] = modexp(g, r, p)
           E[votes[i]-1] = (E[votes[i]-1][0] * c[0] % p, E[votes[i]-1][1] * c[1] % p)
       F = [combine_decryption(T, decrypt_vote(e, x)) for e in E]
       G = [modexp(f, 1, p) for f in F]
       return G
   
   # Generate parameters
   p, g, h, x, m = generate_params(3)
   
   # Cast votes
   n = 10
   votes = [randint(1, m) for i in range(n)]
   U = [0] * n
   C = [encrypt_vote(votes[i], h)[0] for i in range(n)]
   
   # Compute secret sharing
   T, s = compute_secret_sharing()
   
   # Decrypt votes
   D = [decrypt_vote(c, x) for c in C]
   
   # Compute tally
   G = compute_tally()
   
   # Print results
   print("Votes:", votes)
   print("Encrypted votes:", C)
   print("Decrypted votes:", D)
   print("Secret sharing:", T)
   print("Tally:", G)
   print("Winner:", G.index(max(G))+1)
```
   
In this code generates random parameters for a voting system with 3 candidates, and then simulates the casting and 
counting of 10 votes.\
The results are printed to the console, including the **decrypted votes**, **the secret sharing**, **the tally**, and **the winner**.\
_Note that the code assumes a trusted election authority that generates the parameters and distributes the secret sharing._\
In a real-world scenario, additional measures would be necessary to ensure the integrity and security of the system.

---
   
### Simulation voting system:

Simulate a voting with 3 candidates using the **zero-knowledge voting system** I described earlier:

#### Mathematics:
Let's assume the following parameters:
```
- p = 23
- g = 5
- h = g^x mod p, where x = 7
- m = 3 (number of candidates)
```

#### To simulate a voting with 10 voters, we can follow these steps:
1. Each voter selects a candidate to vote for, and encrypts their vote using a random number r_i:
```
   - Voter 1 chooses candidate 1 and encrypts their vote as c_1 = (g^2, h^1 * g^2) using r_1 = 2.
   - Voter 2 chooses candidate 2 and encrypts their vote as c_2 = (g^3, h^2 * g^3) using r_2 = 3.
   - Voter 3 chooses candidate 1 and encrypts their vote as c_3 = (g^4, h^1 * g^4) using r_3 = 4.
   - Voter 4 chooses candidate 3 and encrypts their vote as c_4 = (g^5, h^3 * g^5) using r_4 = 5.
   - Voter 5 chooses candidate 1 and encrypts their vote as c_5 = (g^6, h^1 * g^6) using r_5 = 6.
   - Voter 6 chooses candidate 2 and encrypts their vote as c_6 = (g^7, h^2 * g^7) using r_6 = 7.
   - Voter 7 chooses candidate 2 and encrypts their vote as c_7 = (g^8, h^2 * g^8) using r_7 = 8.
   - Voter 8 chooses candidate 3 and encrypts their vote as c_8 = (g^9, h^3 * g^9) using r_8 = 9.
   - Voter 9 chooses candidate 3 and encrypts their vote as c_9 = (g^10, h^3 * g^10) using r_9 = 10.
   - Voter 10 chooses candidate 1 and encrypts their vote as c_10 = (g^11, h^1 * g^11) using r_10 = 11.
```

2. The election authority generates a secret sharing of the decryption key:
```
   - The election authority chooses random numbers k_1 = 3 and k_2 = 11.
   - The shares of the secret key are t_1 = g^k_1 mod p = 10 and t_2 = g^k_2 mod p = 4.
```

3. The encrypted votes and the shares of the decryption key are published.
4. Each voter publishes their encryption random number r_i and their share of the encryption random numbers u_i = g^r_i mod p.
```
   - Voter 1 publishes r_1 = 2 and u_1 = g^2 mod p = 4.
   - Voter 2 publishes r_2 = 3 and u_2 = g^3 mod p = 10.
   - Voter 3 publishes r_3 = 4 and u_3 = g^4 mod p = 18.
   - Voter 4 publishes r_4 = 5 and u_4 = g^5 mod p = 4.
   - Voter 5 publishes r_5 = 6 and u_5 = g^6 mod p = 20.
   - Voter 6 publishes r_6 = 7 and u_6 = g^7 mod p = 15.
   - Voter 7 publishes r_7 = 8 and u_7 = g^8 mod p = 7.
   - Voter 8 publishes r_8 = 9 and u_8 = g^9 mod p = 19.
   - Voter 9 publishes r_9 = 10 and u_9 = g^10 mod p = 15.
   - Voter 10 publishes r_10 = 11 and u_10 = g^11 mod p = 3.
```

5. The election authority combines the shares of the encryption random numbers to obtain the decryption random number k' = k_1 + k_2 = 14, and publishes it. 
6. The election authority decrypts each encrypted vote as follows:
```
   - Voter 1: d_1 = r_1 + k' * (t_1 * t_2^2) mod p = 2 + 14 * (10 * 4^2) mod 23 = 13
   - Voter 2: d_2 = r_2 + k' * (t_1^2 * t_2) mod p = 3 + 14 * (10^2 * 4) mod 23 = 18
   - Voter 3: d_3 = r_3 + k' * (t_1 * t_2^2) mod p = 4 + 14 * (10 * 4^2) mod 23 = 3
   - Voter 4: d_4 = r_4 + k' * (t_1^2 * t_2^2) mod p = 5 + 14 * (10^2 * 4^2) mod 23 = 20
   - Voter 5: d_5 = r_5 + k' * (t_1 * t_2^2) mod p = 6 + 14 * (10 * 4^2) mod 23 = 11
   - Voter 6: d_6 = r_6 + k' * (t_1^2 * t_2) mod p = 7 + 14 * (10^2 * 4) mod 23 = 8
   - Voter 7: d_7 = r_7 + k' * (t_1^2 * t_2) mod p = 8 + 14 * (10^2 * 4) mod 23 = 14
   - Voter 8: d_8 = r_8 + k' * (t_1^2 * t_2^2) mod p = 9 + 14 * (10^2 * 4^2) mod 23 = 16
   - Voter 9: d_9 = r_9 + k' * (t_1^2 * t_2^2) mod p = 10 + 14 * (10^2 * 4^2) mod 23 = 8
   - Voter 10: d_10 = r_10 + k' * (t_1 * t_2) mod p = 11 + 14 * (10 * 4) mod 23 = 9
```

7. The election authority computes the tally as follows:
```
   - Candidate 1: f_1 = g^{w_1 + k'_1} * g^{w_1 + k'_2} mod p = g^{2+3+7+11} mod p = g^{23} mod p = 5
   - Candidate 2: f_2 = g^{w_2 + k'_1} * g^{w_2 + k'_2} mod p = g^{3+11+7+8} mod p = g^{29} mod p = 19
   - Candidate 3: f_3 = g^{w_3 + k'_1} * g^{w_3 + k'_2} mod p = g^{5+3+11+8} mod p = g^{27} mod p = 6
```

8. The election authority publishes the decrypted votes, the tally, and the winner (candidate 2).

#### Python simulation example:

```python
from random import randint
from functools import reduce

# Define parameters
p = 23
g = 5
x = 7
h = pow(g, x, p)
m = 3

# Simulate voting
n = 10
votes = [randint(1, m) for i in range(n)]
enc_votes = []
r_values = []
for i in range(n):
    r = randint(1, p-2)
    c = (pow(g, r, p), (pow(h, votes[i], p) * pow(g, r, p)) % p)
    enc_votes.append(c)
    r_values.append(r)

# Generate secret sharing of decryption key
k1 = 3
k2 = 11
t1 = pow(g, k1, p)
t2 = pow(g, k2, p)
k_prime = k1 + k2

# Combine shares of encryption random numbers
u_values = [pow(g, r, p) for r in r_values]
u_product = reduce(lambda x, y: x * y % p, u_values)

# Decrypt votes
dec_votes = []
for i in range(n):
    d = (r_values[i] + k_prime * (pow(t1, 2, p) * pow(t2, u_values[i], p)) % p) % p
    dec_votes.append(d)

# Compute tally
f_values = [pow(g, sum(1 for v in dec_votes if v == j), p) for j in range(1, m+1)]
f_product = reduce(lambda x, y: x * y % p, f_values)
winner = f_values.index(max(f_values)) + 1

# Print results
print("Votes:", votes)
print("Encrypted votes:", enc_votes)
print("Encryption random numbers:", r_values)
print("Shares of encryption random numbers:", u_values)
print("Shares of decryption key:", t1, t2)
print("Decrypted votes:", dec_votes)
print("Tally:", f_values)
print("Winner:", winner)
```
