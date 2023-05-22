## AES (Advanced Encryption Standard)
AES (Advanced Encryption Standard) is a symmetric-key encryption algorithm used to secure sensitive data. 
AES is based on a substitution-permutation network (SPN) structure where the plaintext is divided into fixed-size blocks and 
each block is transformed using multiple rounds of substitution and permutation operations.

#### The AES algorithm involves the following steps:

1. Key Expansion:
   - Generate a set of round keys from the initial secret key using a key schedule algorithm
   - The round keys are the same size as the block size and are used in each round of the encryption process

2. Encryption:
   - Divide the plaintext message into fixed-size blocks (usually 128 bits)
   - Add the round key to the first block
   - Perform a series of substitution and permutation operations (known as rounds), each round consisting of four transformations: SubBytes, ShiftRows, MixColumns, and AddRoundKey
   - After the final round, output the encrypted ciphertext
   
3. Decryption:
   - Divide the encrypted ciphertext into fixed-size blocks (usually 128 bits)
   - Invert the last round of the encryption process by performing a sequence of inverse transformations: InvShiftRows, InvSubBytes, InvMixColumns, and AddRoundKey
   - Perform the inverse of each of the previous rounds in reverse order
   
#### The mathematical formulas used in AES algorithm:

- Substitution Box (S-Box): A nonlinear substitution function used in AES algorithm to provide confusion. In AES algorithm, the S-Box is a fixed lookup table.
- Permutation Box (P-Box): A linear permutation function used in AES algorithm to provide diffusion. In AES algorithm, the P-Box is a fixed permutation table.
- Round Key Generation: Round key generation algorithm is used to generate the round key for each round of encryption. It involves a combination of substitutions, permutations, AND, XOR operations.
- SubBytes: A substitution operation that replaces each byte of the block with a different byte, using the S-Box.
- ShiftRows: A permutation operation that shifts the rows of the block by a fixed number of bytes, for example, first row is shifted by 0 bytes, second row is shifted by 1 byte, etc.
- MixColumns: A linear operation that mixes the columns of the block using matrix multiplication by a fixed matrix.
- AddRoundKey: An XOR operation that combines the current block with a round key.

#### Example of JavaScript code for AES Encryption and Decryption:

```js
// node-js
const crypto = require('crypto');

// AES Encryption
function aesEncrypt(secretKey, plaintextMsg) {
  const iv = crypto.randomBytes(16); // Generate random initialization vector
  const cipher = crypto.createCipheriv('aes-256-cbc', secretKey, iv);
  let ciphertext = cipher.update(plaintextMsg, 'utf8', 'base64');
  ciphertext += cipher.final('base64');
  return [iv.toString('hex'), ciphertext];
}

// AES Decryption
function aesDecrypt(secretKey, iv, ciphertextMsg) {
  const decipher = crypto.createDecipheriv('aes-256-cbc', secretKey, Buffer.from(iv, 'hex'));
  let plaintext = decipher.update(ciphertextMsg, 'base64', 'utf8');
  plaintext += decipher.final('utf8');
  return plaintext;
}
```

#### Another example:
```js
// nodejs
const crypto = require('crypto');
const algorithm = 'aes-256-cbc';
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16); 

// Encrypt data using AES
function encrypt(text) {
    let cipher = crypto.createCipheriv(algorithm, Buffer.from(key), iv);
    let encrypted = cipher.update(text);
    encrypted = Buffer.concat([encrypted, cipher.final()]);
    return { iv: iv.toString('hex'), encryptedData: encrypted.toString('hex') };
} 

// Decrypt data using AES
function decrypt(text) {
    let iv = Buffer.from(text.iv, 'hex');
    let encryptedText = Buffer.from(text.encryptedData, 'hex');
    let decipher = crypto.createDecipheriv(algorithm, Buffer.from(key), iv);
    let decrypted = decipher.update(encryptedText);
    decrypted = Buffer.concat([decrypted, decipher.final()]);
    return decrypted.toString();
}
```
### Note: 
This is a basic implementation of AES algorithm.

---

### Unofficial "AES-256 encryption" in Solidity, using "CBC mode":
Don't use this code or similar in product, because:
- AES make crash in solidity
- compute memory is to high in solidity

> This code is just for example

```solidity
pragma solidity 0.8;

interface AES256CBC {
    function encrypt(bytes32 key, bytes16 iv, bytes memory plaintext) external pure returns (bytes memory ciphertext);
    function decrypt(bytes32 key, bytes16 iv, bytes memory ciphertext) external pure returns (bytes memory plaintext);
    function getBlock(bytes memory data, uint index) internal pure returns (bytes16);
    function xorBytes(bytes memory a, bytes memory b) internal pure returns (bytes memory result);
}

contract MyContract is AES256CBC {
    function encrypt(bytes32 key, bytes16 iv, bytes memory plaintext) public pure override returns (bytes memory ciphertext) {
        require(plaintext.length % 16 == 0, "Plaintext must be a multiple of 16 bytes");
        ciphertext = new bytes(plaintext.length);
        bytes16[2] memory keystream;
        bytes16 blockIV = iv;
        for (uint i = 0; i < plaintext.length; i += 16) {
            keystream[0] = getBlock(xorBytes(blockIV, key), 0);
            keystream[1] = getBlock(xorBytes(blockIV, key), 1);
            bytes16 blockPT = getBlock(plaintext, i) xor keystream[0];
            blockPT = blockPT xor keystream[1];
            blockIV = blockPT;
            bytes16toBytes(blockPT, ciphertext, i);
        }
    }

    function decrypt(bytes32 key, bytes16 iv, bytes memory ciphertext) public pure override returns (bytes memory plaintext) {
        require(ciphertext.length % 16 == 0, "Ciphertext must be a multiple of16 bytes");
        plaintext = new bytes(ciphertext.length);
        bytes16[2] memory keystream;
        bytes16 blockIV = iv;
        for (uint i = 0; i < ciphertext.length; i += 16) {
            keystream[0] = getBlock(xorBytes(blockIV, key), 0);
            keystream[1] = getBlock(xorBytes(blockIV, key), 1);
            bytes16 blockCT = getBlock(ciphertext, i);
            blockCT = blockCT xor keystream[1];
            blockCT = blockCT xor keystream[0];
            blockIV = getBlock(ciphertext, i);
            bytes16toBytes(blockCT, plaintext, i);
        }
    }

    function getBlock(bytes memory data, uint index) internal pure override returns (bytes16) {
        require(data.length >= (index + 1) * 16, "Data array too short");
        bytes16 block;
        assembly {
            block := mload(add(add(data, 16), mul(index, 16))))
        }
        return block;
    }

    function xorBytes(bytes memory a, bytes memory b) internal pure override returns (bytes memory result) {
        require(a.length == b.length, "Byte arrays must be of equal length");
        result = new bytes(a.length);
        for (uint i = 0; i < a.length; i++) {
            result[i] = a[i] xor b[i];
        }
    }

    function bytes16toBytes(bytes16 input, bytes memory output, uint offset) internal pure {
        assembly {
            mstore8(add(output, add(offset, 0)), byte(15, input))
            mstore8(add(output, add(offset, 1)), byte(14, input))
            mstore8(add(output, add(offset, 2)), byte(13, input))
            mstore8(add(output, add(offset, 3)), byte(12, input))
            mstore8(add(output, add(offset, 4)), byte(11, input))
            mstore8(add(output, add(offset, 5)), byte(10, input))
            mstore8(add(output, add(offset, 6)), byte(9, input))
            mstore8(add(output, add(offset, 7)), byte(8, input))
            mstore8(add(output, add(offset, 8)), byte(7, input))
            mstore8(add(output, add(offset, 9)), byte(6, input))
            mstore8(add(output, add(offset, 10)), byte(5, input))
            mstore8(add(output, add(offset, 11)), byte(4, input))
            mstore8(add(output, add(offset, 12)), byte(3, input))
            mstore8(add(output, add(offset, 13)), byte(2, input))
            mstore8(add(output, add(offset, 14)), byte(1, input))
            mstore8(add(output, add(offset, 15)), byte(0, input))
        }
    }
}
```
