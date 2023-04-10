## Phi (Φ) function - Euler's totient
Phi (Φ) function, also known as Euler's totient function, is an arithmetic function that counts the positive integers up to 
a given integer n that are relatively prime to n. In other words, the function returns the number of integers from 1 to n-1 that 
have no common factor with n other than 1.

The phi function is written as Φ(n) or ϕ(n). Here are the mathematical formulas to calculate phi function:

1. If p is a prime number, then `Φ(p) = p − 1`

2. If p and q are distinct prime numbers, then `Φ(pq) = (p − 1)(q − 1)`

3. For a general n, let p1, p2, ..., pm be the distinct prime factors of n. Then, 

   `Φ(n) = n * (1-1/p1) * (1-1/p2) * ... * (1-1/pm)`
   
#### Example of JavaScript code to calculate phi function Φ(n):

```js
// Compute phi function Φ(n)
function phi(n) {
    let result = n; // Initialize result with n
    
    // Check for all prime factors smaller or equal to sqrt(n)
    for (let i = 2; i*i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
            }
            result -= (result / i);
        }
    }
    
    // If n has a prime factor greater than sqrt(n)
    if (n > 1) {
        result -= (result / n);
    }

    return result;
}
```

### Note: 
This implementation of phi function uses a well-known algorithm called Euler’s Totient Function Formula.

#

### Funny time:
Christian Goldbach in a letter to the Euler make a discusion. The "Goldbach Conjecture" [read more](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) 
- 2m = p + q
- p >= m
- q <= m

He calculate the chance of q & p are be prime number ...\
Calculation power speed = ( ln n ≪ √n )

![formmula graph](https://upload.wikimedia.org/wikipedia/commons/7/7c/Goldbach-1000000.png)
