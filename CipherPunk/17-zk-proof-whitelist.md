The code in below in "Solidity" for presenting **ZK-Proof Whitelist** idea:

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
