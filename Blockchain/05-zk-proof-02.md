### Example 2 : 
Here is an example of a simple ZKP algorithm in pseudo code:

```js
// Prover wants to prove they know the secret number x 
// Verifier wants to verify that the Prover knows x without revealing x 
// Step 1: Prover selects a random number r and computes y = r^2 mod N, where N is a large prime 
r = random_number() 
y = (r * r) % N 

// Step 2: Prover sends y to Verifier 
send(y) 

// Step 3: Verifier sends a random challenge c to the Prover 
c = random_number() 
send(c) 

// Step 4: Prover computes z = r if c = 0, or z = r * x if c = 1, and sends z to Verifier 
if (c == 0): 
  z = r 
else: 
  z = (r * x) % N 
send(z) 

// Step 5: Verifier checks if y = z^2 mod N if c = 0 
// , or if y * x = z^2 mod N if c = 1 

if (c == 0): 
  if ((z * z) % N == y): 
    accept_proof() 
  else: reject_proof() 
else: 
  if ((z * z * x) % N == y): 
    accept_proof() 
  else: reject_proof()
```

In this example, the Prover wants to prove that they know the secret number `x` to the Verifier, without revealing `x`. The Prover selects a random number `r` and computes `y = r^2` mod `N`, where `N` is a large prime. They send `y` to the Verifier.

The Verifier then sends a random challenge `c` to the Prover. The Prover computes `z = r` if `c = 0`, or `z = r * x` if `c = 1`, and sends z to the Verifier.

The Verifier checks if `y = z^2` mod `N` if `c = 0`, or if `y * x = z^2` mod `N` if `c = 1`. If the check passes, the Verifier accepts the proof; otherwise, they reject it. If the proof is accepted, the Verifier knows that the Prover knows the secret number `x`, but they do not know the value of `x` itself.

This is a simple example of a ZKP algorithm, and in practice, more complex algorithms are used for more sophisticated proofs.

#

#### Remember: 
many solution about the zk-proof has been made before 1990! so think out of the box and create new solution for any situation to make better world...
