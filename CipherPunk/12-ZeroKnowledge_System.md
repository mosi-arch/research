## "solution algorithm" : how to make a voting system, by "zero knowledge" for voter.

1. Define the problem: 
   We want to create a voting system where voters can cast their votes anonymously, without revealing their identities or 
   the contents of their votes to anyone, while ensuring that each vote is counted exactly once and that the final result is correct.

2. Design the system: 
   We can use a combination of cryptographic techniques, such as **homomorphic encryption**, **zero-knowledge proofs**, and 
   verifiable secret sharing, to achieve our goal.

3. Define the mathematical formula: 
   
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

4. Write the Python code:
   Here is a possible Python implementation of the above formula:
   
   ````python
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
   
