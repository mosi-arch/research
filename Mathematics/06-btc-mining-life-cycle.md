# BTC Mining Life Cycle

### Mathematics behind the (POW in Bitcoin)
Bitcoin mining never end up: each 4 years the mining result halved. 
- So the equation is = **-1 / 12**
- The infinite life time cycle of work and never finish.
- **8/π^4≈0, 1/12, 5/61, 6/73,** ... (simple continued fraction convergent sequence)

#### Similar equations:
- ≈ -**0.0833333**
- ≈ -**(833333 / 10000000)**
- ≈ -**(10Pi / 377)**
- ≈ -**(1 / 12)**

### In Euclidean mathematics: 
This equation means that every 4-year period, the radius of the circle is added to the previous diameter.\
That is, circle radius + circle diameter is equal to the new circle. (tao **τ** = 2pi **2π**)\
The distance between you and the destination increases, in the second dimension.\
The third dimension (3d = sphare) of this equation is different.

### In linear algebra: 
In each 4-year period, you travel half the distance of the previous period.\
A line by width *21.000.000* each period half of the distance.

#

#### Simple equetion
Point of View: satoshies * 0.5 ^ n = 0\
Build a loop and compute the cycles,\
each cycle * 4 = how many years.\
n represnting the cycles.

- 21000000 * (1/2)^(n) = 0

P.S: remember to calculate Satoshies (0.00000001 BTC)\
1 BTC = 1000000000 satoshi

#

## Logic of Equetion [ theorem ]
To solve this equation for 'n', we can use logarithms.\
First, we can simplify the left side of the equation by dividing both sides by '210000' (210000 is short hand number for present 21Million):\
`0.5^n = 0/210000` 

'0/210000' is equal to '0' **:) !**, so we can rewrite the equation as:\
`0.5^n = 0` 

Now we can take the logarithm base '0.5' of both sides:\
`log_0.5(0.5^n) = log_0.5(0)` 

The right side of the equation is undefined, so the equation has no solution.\
Therefore, there is no value of n for which `210000 * 0.5 ^ n = 0`.

:)

#### Example JavaScript code:
- this code generate a text file and show you 1000 period (each one is 4 years)
- generated file [here](https://github.com/mosi-arch/research/blob/main/Documents/BTC-After_4000Years.txt)

```js
// nodejs
const fs = require('fs');

function calculateLTFiftyPct(n) {
  return 21000000 * Math.pow(0.5, n); // 21000000 for btc, for including satoshi use: 21000000x10000000 (21e13)
}

let answer = [];

for (let n = 1; n <= 1000; n++) {
  let lt = calculateLTFiftyPct(n);
  if (lt > 0) {
    answer.push(lt);
  } else {
    break; // break out of loop if lt <= 0
  }
}

fs.writeFileSync('answer.txt', answer.join('\n'));
console.log('Answer saved to answer.txt');
```

#### example for period 1 to 1000:
- Period 1: `10500000`
- Period 2: `5250000`
- Period 3: `2625000`
- ...
- Period 24: `1.2516975` BTC
- ...
- Period 998: `7.839414395427039e-294`
- Period 999: `3.919707197713519e-294`
- Period 1000: `1.9598535988567596e-294`

Each period is 4 years, so we calculating 4000 years!!!\
After period 24 (24 x 4 years) the number of mining near the 1, after that we have satoshies.\
The Period 1000 show us a big number, but that more then '0' [1.959854e-294] but satoshi is 0.00000001. so calculate yourself and watch the answer!\
Maybe community make fraction on satoshies, meybe not. Anyway the equation show us BTC mining can run forever :)

---

### Fun fact!
How "Lord Satoshi Nakamoto" calculated the limitation of each period?\
Equation is: **∞∑(n=0) 1/(2^n)**\
**|x| = 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^n) = 2** (limit is 2)\
So each period hardest 2 times from the previus period!!!

- In "Riemann zeta function" 'n=1' -> `ς(s) = ∞∑(n=1) ...` this is make same value like satoshi sequence, but for create 'life cycle' not for limitation. because this equetion generative and interactive :)
  - the answer of this equetion is '(-1)/12'
  - euler proof this interactive '(s)' by -> '(pi^2)/6', before the riemann idea!
