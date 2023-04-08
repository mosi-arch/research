-- README.md
## Cipher & Decipher use for generating key
**xor** make magic, if key is a **prime number**. look at this example psuedo:

```solidity
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.0 <0.9.0;

library BitwiseLib {
    function xor(uint a, uint b) pure internal returns (uint x, bytes32 y) {
        x = a^b; // x = bool(a) ^ bool(b) == 1 
        y = keccak256(abi.encodePacked(x)); // encodePacked method not have unnecesory " 0 "
    }
    
    function and(uint a, uint b) pure internal returns (uint x) {
        x = a&b;
    }
    
    function or(uint a, uint b) pure internal returns (uint x) {
        x = a|b;
    }
    
    function not(uint a) pure internal returns (uint x) {
        x = ~a;
    }
}

// test to cipher/decipher by using bitwise operation "xor" (xor sign in solidity is carrot " ^ ")
contract Xor {
    using BitwiseLib for uint;
    
    // type: import library
    function xor1(uint a, uint b) pure public returns (uint x, bytes32 y) {
        (x, y) = BitwiseLib.xor(a,b);
    }
    
    // type: using include library
    function xor2(uint a, uint b) pure public returns (uint x, bytes32 y) {
        (x, y) = a.xor(b);
    }
}
```

deploy "Xor" contract and following the rules.
```js
cipher:
input : a = 99121112104101114112117110107
input : b = 1000000000000066600000000000001

output : uint256 x = 1099111320276219782373852476762
output : bytes32 y = 0x36d7a50085e421c5578e8978df08e7684b66d5dadbd8ee2791777c9715f5e6d5

decipher: 
uint i = x xor b
(i == a) === true
```

note: 
- **b** is the **key** for cipher & deciphering
- **b** would/shuld/must/always be a prime number
- **y** can use for **private key**, this example make address: `0x6f3988E36894a57188114ad5DE236a9Cb4cEEE18`

fun information:
- can you decipher **a** (example variable **a**)? have the surprise for you!
- did you know "variable **b**" is a prime number and have this name -> "Evil Prime number" 

disclaimer:
- dont use this type of private key, because can decipher to resurces.
- every number power to " 0 " is " 1 ". this method to hack binaries.
- we use hashing algorithms [fixed size, example size(bytes32) = length] to be safe of these danger zones.

tips:
- in binary equations meybe "overflow" happend. so we use module of answer.

---

## Simulator (ram)
using 'BitwiseLib' library
```solidity
contract BitTest {
    using BitwiseLib for uint;
    event listen(uint,uint,uint,uint,uint,uint,bytes32,uint,uint);
        
    // simulator not immune
    function ram(uint a, uint b) public returns (uint x, bytes32 y, uint position) {
        // ram simulation start
        uint i = a.not();
        uint j = b.not();
        uint h2o = a.and(j); // return a
        uint co2 = b.and(i); // return b
        uint fin = h2o.or(co2); // sum a + b
        // ram simulation finish

        fin > a ? 
        x = uint(keccak256(abi.encode(fin.and(fin)))) : 
        x = uint(keccak256(abi.encode(fin.or(fin))));

        // bytes32 why = keccak256(abi.encode(fin.not()));
        y = keccak256(abi.encode(fin.not()));
        uint r = x % uint(y);
        // ( ,y) = uint(why).xor(r); // buffer overflow
        position = r % 16; // translate this line = biggest bug of EVM. hackers can guess you!
        
        emit listen(i,j,h2o,co2,fin,x, y, r, position);
    }
}
```
two usecase for variable output "position"
#### A.
position cheat sheet (hex maker) :
- 0 to 9 positions exactly same of the number
- 10 = a | 11 = b | 12 = c | 13 = d | 14 = e | 15 = f......

#### B.
ram simulation example :
```js
"i": "115792089237316195423570985008687907853269984665640564039457584007913129639925",
"j": "115792089237316195423570985008687907853269984665640564039457584007913129639915",
"h2o": "10",
"co2": "20",
"fin": "30",
"x": "36516136433507714556481507284757523525550975291680945358964353894568634540880",
"y": "0x1da15cb88d2f0e1be9290c6933bb2e8c6359799e06fcd6e5d8969b8e59e32c46",
"r": "9711786588494660349237493733220162383806500538113175522243601272905808251588",
"position": "4"  --> always a rythm exist for guess (snif). evm not immune
```

if output variable 'y' using 'xor' by any key, the code overflow memory buffer and code will be break.
