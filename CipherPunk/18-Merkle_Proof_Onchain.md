### Merkle Proof Onchain
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MerkleProof {
    /**
    * @dev Verifies a Merkle proof.
    * @param root The root of the Merkle tree.
    * @param leaf The leaf node being proven.
    * @param proof The Merkle proof.
    * @param offset The offset of the leaf in the Merkle tree.
    * @return true if the proof is valid, false otherwise.
    */
    function verify(bytes32 root, bytes32 leaf, bytes32[] memory proof, uint256 offset) public pure returns (bool) {
        bytes32 computedHash = leaf;
        uint256 proofIndex = offset;
        for (uint256 i = 0; i < proof.length; i++) {
            bytes32 proofElement = proof[i];

            if (proofIndex % 2 == 0) {
                computedHash = keccak256(abi.encodePacked(computedHash, proofElement));
            } else {
                computedHash = keccak256(abi.encodePacked(proofElement, computedHash));
            }

            proofIndex = proofIndex / 2;
        }

        return computedHash == root;
    }
    
    /*function getRoot(bytes32[] memory leaves) public pure returns (bytes32) {
        uint256 n = leaves.length;
        uint256 depth = ceilLog2(n);

        bytes32[] memory nodes = new bytes32[](2 * n - 1);
        for (uint256 i = 0; i < n; i++) {
            nodes[n - 1 + i] = leaves[i];
        }

        for (uint256 i = n - 2; i >= 0; i--) {
            nodes[i] = keccak256(abi.encodePacked(nodes[2 * i + 1], nodes[2 * i + 2]));
        }

        return nodes[0];
    }*/

    /**
    * @dev Calculates the Merkle root given a set of leaves.
    * @param data The array of leaves.
    * @return The Merkle root.
    */
    function getRoot(bytes32[] memory data) public pure returns (bytes32) {
        require(data.length > 0, "MerkleTree: empty data");

        uint256 n = data.length;
        uint256 depth = ceilLog2(n);

        bytes32[] memory leaves = new bytes32[](2**depth);

        for (uint256 i = 0; i < n; i++) {
            leaves[i] = data[i];
        }

        for (uint256 i = n; i < 2**depth; i++) {
            leaves[i] = bytes32(0);
        }

        for (uint256 i = depth; i > 0; i--) {
            for (uint256 j = 0; j < 2**(i - 1); j++) {
                uint256 k = 2**i - 2**(i - 1) + j;
                leaves[k] = keccak256(abi.encodePacked(leaves[2 * k + 1], leaves[2 * k + 2]));
            }
        }

        return leaves[0];
    }
    
    function ceilLog2(uint256 x) internal pure returns (uint256) {
        uint256 y = x;
        uint256 i;
        for (i = 0; y > 0; i++) {
            y >>= 1;
        }
        return i;
    }
}

// ====================================================

contract MerkleTree {
    /**
    * @dev Calculates the Merkle root given an array of bytes.
    * @param data The array of bytes.
    * @return The Merkle root.
    */
    function getRoot(bytes[] memory data) public pure returns (bytes32) {
        require(data.length > 0, "MerkleTree: empty data");

        uint256 n = data.length;
        bytes32[] memory leaves = new bytes32[](n);

        for (uint256 i = 0; i < n; i++) {
            leaves[i] = sha256(data[i]);
        }

        while (n > 1) {
            uint256 m = (n + 1) / 2;

            for (uint256 i = 0; i < m; i++) {
                uint256 j = 2 * i;
                if (j + 1 == n) {
                    leaves[i] = keccak256(abi.encodePacked(leaves[j], leaves[j]));
                } else {
                    leaves[i] = keccak256(abi.encodePacked(leaves[j], leaves[j + 1]));
                }
            }

            n = m;
        }

        return leaves[0];
    }

    /**
    * @dev Calculates the Merkle root given an array of addresses.
    * @param addresses The array of addresses.
    * @return The Merkle root.
    */
    function getRoot(address[] memory addresses) public pure returns (bytes32) {
        require(addresses.length > 0, "MerkleTree: empty addresses");

        uint256 n = addresses.length;
        bytes32[] memory leaves = new bytes32[](n);

        for (uint256 i = 0; i < n; i++) {
            leaves[i] = bytes32(uint256(keccak256(abi.encodePacked(addresses[i]))));
        }

        while (n > 1) {
            uint256 m = (n + 1) / 2;

            for (uint256 i = 0; i < m; i++) {
                uint256 j = 2 * i;
                if (j + 1 == n) {
                    leaves[i] = keccak256(abi.encodePacked(leaves[j], leaves[j]));
                } else {
                    leaves[i] = keccak256(abi.encodePacked(leaves[j], leaves[j + 1]));
                }
            }

            n = m;
        }

        return leaves[0];
    }

}
```

---

## Documents

### verify

```solidity
/**
 * @dev Verifies a Merkle proof.
 * @param root The root of the Merkle tree.
 * @param leaf The leaf node being proven.
 * @param proof The Merkle proof.
 * @param offset The offset of the leaf in the Merkle tree.
 * @return true if the proof is valid, false otherwise.
 */
function verify(bytes32 root, bytes32 leaf, bytes32[] memory proof, uint256 offset) public pure returns (bool)
```

This function verifies a Merkle proof for a given leaf node. It takes in the following parameters:

- `root`: the root hash of the Merkle tree.
- `leaf`: the leaf node being proven.
- `proof`: the Merkle proof for the leaf node.
- `offset`: the offset of the leaf node in the Merkle tree.

It returns a boolean value indicating whether the proof is valid or not.

### getRoot

```solidity
/**
 * @dev Calculates the Merkle root given a set of leaves.
 * @param data The array of leaves.
 * @return The Merkle root.
 */
function getRoot(bytes32[] memory data) public pure returns (bytes32)
```

This function calculates the Merkle root of a set of leaves. It takes in an array of leaves as the `data` parameter and returns the Merkle root hash.

#

### getRoot (bytes)

```solidity
/**
 * @dev Calculates the Merkle root given an array of bytes.
 * @param data The array of bytes.
 * @return The Merkle root.
 */
function getRoot(bytes[] memory data) public pure returns (bytes32)
```

This function calculates the Merkle root of an array of bytes. It takes in an array of bytes as the `data` parameter and returns the Merkle root hash.

### getRoot (addresses)

```solidity
/**
 * @dev Calculates the Merkle root given an array of addresses.
 * @param addresses The array of addresses.
 * @return The Merkle root.
 */
function getRoot(address[] memory addresses) public pure returns (bytes32)
```

This function calculates the Merkle root of an array of Ethereum addresses. It takes in an array of addresses as the `addresses` parameter and returns the Merkle root hash. The addresses are first converted to bytes before being hashed.
