### The codes in below in "Solidity" for presenting **ZK-Proof Whitelist** idea:

- example 1:
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

- example 2:
```solidity
pragma solidity ^0.8.0;

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

        // Initialize ZoKrates verifier contract
        IVerifier verifier = IVerifier(0x0000000000000000000000000000000000000000); // Replace with actual verifier contract address

        // Initialize ZoKrates proof contract
        IProof proof = IProof(0x0000000000000000000000000000000000000000); // Replace with actual proof contract address

        // Generate proof using ZoKrates
        (uint256[] memory proofInputs, uint256[] memory proofOutputs) = proof.generateProof(input);

        // Verify proof using ZoKrates verifier
        return verifier.verifyProof(_proof.a, _proof.b, proofInputs, proofOutputs);
    }
    */
    
    function verifyProof(address addressToVerify, Proof memory _proof, address verifierAddress, address proofAddress) internal view returns (bool) {
        uint256[] memory input = new uint256[](2);
        input[0] = uint256(addressToVerify);
        input[1] = whitelist[addressToVerify];

        // Initialize ZoKrates verifier contract
        IVerifier verifier = IVerifier(verifierAddress);

        // Initialize ZoKrates proof contract
        IProof proof = IProof(proofAddress);

        // Generate proof using ZoKrates
        (uint256[] memory proofInputs, uint256[] memory proofOutputs) = proof.generateProof(input);

        // Verify proof using ZoKrates verifier
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
