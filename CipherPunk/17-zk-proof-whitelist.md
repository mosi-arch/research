### The codes in below in "Solidity" for presenting **ZK-Proof Whitelist** idea:

#### example 1:
```solidity
pragma solidity 0.8;

contract Whitelist {
    mapping(address => bool) private _whitelist;

    function addToWhitelist() external {
        _whitelist[msg.sender] = true;
    }

    function removeFromWhitelist() external {
        _whitelist[msg.sender] = false;
    }

    function isWhitelisted(address addr) public view returns (bool) {
        return _whitelist[addr];
    }
}

contract Claimable is Whitelist {
    bytes32 private constant CLAIM_HASH = keccak256("claim");

    function claim(uint256 amount, bytes memory proof) external {
        require(isWhitelisted(msg.sender), "Sender is not whitelisted");

        bytes32 proofHash = keccak256(proof);
        require(proofHash == CLAIM_HASH, "Invalid proof");

        // Perform claim logic here
    }
}
```

#### example 2:
```solidity
pragma solidity 0.8;

library BitwiseMask {
    function setBit(uint256 mask, uint256 bit) internal pure returns (uint256) {
        return mask | (1 << bit);
    }

    function clearBit(uint256 mask, uint256 bit) internal pure returns (uint256) {
        return mask & ~(1 << bit);
    }

    function hasBit(uint256 mask, uint256 bit) internal pure returns (bool) {
        return (mask & (1 << bit)) != 0;
    }
}

contract Whitelist {
    using BitwiseMask for uint256;

    struct Proof {
        uint256 a;
        uint256 b;
    }

    mapping(address => uint256) public whitelist;
    mapping(address => Proof) public proofs;

    function addToWhitelist(address[] calldata addresses, Proof[] calldata _proofs) external {
        require(addresses.length == _proofs.length, "Invalid input");

        for (uint256 i = 0; i < addresses.length; i++) {
            require(verifyProof(addresses[i], _proofs[i]), "Invalid proof");

            whitelist[addresses[i]] = whitelist[addresses[i]].setBit(0);
        }
    }

    function removeFromWhitelist(address[] calldata addresses) external {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = whitelist[addresses[i]].clearBit(0);
        }
    }

    /*
    function verifyProof(address addressToVerify, Proof memory _proof) internal view returns (bool) {
        uint256[] memory input = new uint256[](2);
        input[0] = uint256(addressToVerify);
        input[1] = whitelist[addressToVerify];

        // Initialize verifier contract
        IVerifier verifier = IVerifier(0x0000000000000000000000000000000000000000); // Replace with actual verifier contract address

        // Initialize proof contract
        IProof proof = IProof(0x0000000000000000000000000000000000000000); // Replace with actual proof contract address

        // Generate proof
        (uint256[] memory proofInputs, uint256[] memory proofOutputs) = proof.generateProof(input);

        // Verify proof using verifier
        return verifier.verifyProof(_proof.a, _proof.b, proofInputs, proofOutputs);
    }
    */
    
    function verifyProof(address addressToVerify, Proof memory _proof, address verifierAddress, address proofAddress) internal view returns (bool) {
        uint256[] memory input = new uint256[](2);
        input[0] = uint256(addressToVerify);
        input[1] = whitelist[addressToVerify];

        // Initialize verifier contract
        IVerifier verifier = IVerifier(verifierAddress);

        // Initialize proof contract
        IProof proof = IProof(proofAddress);

        // Generate proof
        (uint256[] memory proofInputs, uint256[] memory proofOutputs) = proof.generateProof(input);

        // Verify proof using verifier
        return verifier.verifyProof(_proof.a, _proof.b, proofInputs, proofOutputs);
    }

    function canClaim(address addressToCheck) external view returns (bool) {
        return whitelist[addressToCheck].hasBit(0);
    }
}

interface IVerifier {
    function verifyProof(uint256 a, uint256 b, uint256[] calldata input, uint256[] calldata output) external view returns (bool);
}

interface IProof {
    function generateProof(uint256[] calldata input) external view returns (uint256[] memory inputs, uint256[] memory outputs);
}
```

#### example 3 (verifier, proof):
```solidity
pragma solidity 0.8;

contract ZKProof {
    uint256 private constant p = 115792089237316195423570985008687907853269984665640564039457584007908834671663;
    uint256 private constant q = 28948022309329048855892746252171976963317496166410141009864396001978282409983;
    uint256 private constant g = 2;
    uint256 private constant h = 3;

    struct Proof {
        uint256 a;
        uint256 b;
    }

    function verify(uint256 x, Proof memory proof) public view returns (bool) {
        require(proof.a > 0 && proof.a < p, "Invalid proof a");
        require(proof.b > 0 && proof.b < q, "Invalid proof b");

        uint256 lhs = modexp(g, x, p);
        uint256 rhs = modexp(h, proof.a, p) * modexp(proof.b, q, p) % p;

        return lhs == rhs;
    }

    function modexp(uint256 base, uint256 exponent, uint256 modulus) internal pure returns (uint256) {
        uint256 result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = mulmod(result, base, modulus);
            }
            base = mulmod(base, base, modulus);
            exponent = exponent / 2;
        }
        return result;
    }

    function prove(uint256 x, uint256 r) public view returns (Proof memory) {
        uint256 a = modexp(g, r, p);
        uint256 b = (modexp(h, r, p) * modexp(g, x.mulmod(r, q).mod(q), p)).mod(q);

        return Proof(a, b);
    }
}
```

formula used in this code:
- g^x = h^a * b^q (mod p)
- a = g^r (mod p) 
- b = h^r * g^(x*r mod q) (mod p)
- Important notice: `p` and `q` in this code is example, never use this two directly in smartcontract, use "oracle" to provide them.
- `p` and `q` are the big prime numbers.
