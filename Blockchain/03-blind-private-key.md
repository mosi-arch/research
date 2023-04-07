# generate private key, blind method 
how to generate private key for make public key and wallet address.\
example psuedo code:
```js
p = random()
q = random()
t = p * q

x = t % p
y = q % x

private_wallet = hash(y)
```

example output:
```js
p = 655061542424384900
q = 671120875099921200
t = 4.396254755961573e+35
x = 391863794422382340
y = 279257080677538800
// solidity -> bytes32 prvKey = keccak256(abi.encodPacked(y))

private key = 0x96ee4fda279de09402bddb98502e5638562fcc4cf5385935810c437fc2ce3f8c
public key = 0xb5a386eb2b58d1a66a1aad3beca6e139e87075d567dbfb67640a9c7e6abafbd99c9013a7b06d3a84bf1bb6aef1f9bed9c19824873029d953928fa8202d9bb03c
address = 0x9060e832a21c1b04dca33ebf8b827504bb0000fe
// address is hash code of public key. example in your wallet, look at that
```

this private key work & generate the address on this code, but not add to your wallet.\
disclaimer: do not using this example private key on your product.

#

example 2 & 3
```js
h1 = hash() // 0x96ee4fda279de09402bddb98502e5638562fcc4cf5385935810c437fc2ce3f8c
// use hash is/as private key

// prv - pub - address
prv = h1.private 
// 0x96ee4fda279de09402bddb98502e5638562fcc4cf5385935810c437fc2ce3f8c
pub = h1.public 
// 0xb5a386eb2b58d1a66a1aad3beca6e139e87075d567dbfb67640a9c7e6abafbd99c9013a7b06d3a84bf1bb6aef1f9bed9c19824873029d953928fa8202d9bb03c
addr = h1.address 
// 0x9060e832a21c1b04dca33ebf8b827504bb0000fe

//-----------------
/* method 1 */
r1 = prv & pub
r2 = prv | pub
s1 = r1 * r2
s2 = r1 % r2
s3 = s1 % s2
h2 = hash(s3) // 0x82fefdfa979f63867aeff0e17967557b9a65473fb8afeaa43699c678592486aa
// use h2 is/as private key

//-----------------
/* method 2 */
h3 = hash(pub) // 0x2aef511f5415c831fe76ebd01455374e84f84b040481ce8977697cf4e93a1ec8
r10 = addr & h3
r20 = addr | h3
s10 = r10 % r20
h4 = hash(s10) // 0xebe5ad1b5fc5491a177f1270b784df723b033ef508606c10aa1528d31376be05
// use h4 is/as private key
```

why using " & " , "  | " ?\
just for reverting positions\
another disclaimer: this document have purpose to learn developers nice things about cryptography/blockchain!
