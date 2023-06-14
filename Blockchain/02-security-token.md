## Example solidity code about "Security token for identification", by full information
Security token contract that can be used for identification purposes:
```solidity
pragma solidity ^0.8.0;
contract SecurityToken {

  string public name;
  string public symbol;
  uint256 public totalSupply;
  mapping(address => uint256) public balanceOf;
  mapping(address => mapping(address => uint256)) public allowance;

  event Transfer(address indexed from, address indexed to, uint256 value);
  event Approval(address indexed owner, address indexed spender, uint256 value);

  constructor(string memory _name, string memory _symbol, uint256 _totalSupply) {
    name = _name;
    symbol = _symbol;
    totalSupply = _totalSupply;
    balanceOf[msg.sender] = _totalSupply;
  }

  function transfer(address _to, uint256 _value) public returns (bool success) {
    require(balanceOf[msg.sender] >= _value, "Insufficient balance");
    balanceOf[msg.sender] -= _value;
    balanceOf[_to] += _value;
    emit Transfer(msg.sender, _to, _value);
    return true;
  }

  function approve(address _spender, uint256 _value) public returns (bool success) {
    allowance[msg.sender][_spender] = _value;
    emit Approval(msg.sender, _spender, _value);
    return true;
  }

  function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
    require(_value <= balanceOf[_from], "Insufficient balance");
    require(_value <= allowance[_from][msg.sender], "Insufficient allowance");
    balanceOf[_from] -= _value;
    balanceOf[_to] += _value;
    allowance[_from][msg.sender] -= _value;
    emit Transfer(_from, _to, _value);
    return true;
  }
}
```

This contract defines a standard ERC-20 token with the name, symbol, and total supply specified in the constructor. Users can transfer tokens to each other and approve other addresses to spend their tokens on their behalf.

This contract can be used for identification purposes by assigning a unique token to each user and verifying ownership of that token. For example, a user could be required to send a small amount of their token to a verification contract to prove that they own it.

#

### Security token that uses ERC721 from the OpenZeppelin library:
```solidity
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SecurityToken is ERC721 {
  constructor(string memory name, string memory symbol) ERC721(name, symbol) {}
  
  struct Identification {
    string name;
    uint256 id;
    address issuer;
  }
  
  mapping (uint256 => Identification) identifications;
  
  function issueIdentification(uint256 tokenId, string memory name) public {
    require(msg.sender == ownerOf(tokenId), "You are not the owner of this token.");
    require(identifications[tokenId].id == 0, "This token already has an identification.");
    identifications[tokenId] = Identification(name, tokenId, msg.sender);
  }
  
  function getIdentification(uint256 tokenId) public view returns (string memory, uint256, address) {
    require(identifications[tokenId].id != 0, "This token does not have an identification.");
    Identification memory identification = identifications[tokenId];
    return (identification.name, identification.id, identification.issuer);
  }
}
```

This contract inherits from `ERC721`, which provides the standard functionality for non-fungible tokens. The contract includes a `Identification` struct to store information about the token's identification, and a mapping to keep track of which tokens have an identification. The `issueIdentification` function allows the owner of a token to issue an identification for it, and the `getIdentification` function allows anyone to retrieve the identification for a given token.

---

At the end, the [erc-1450](https://eips.ethereum.org/EIPS/eip-1450) a big looser!\
and [erc-1462](https://eips.ethereum.org/EIPS/eip-1462) using just for fractional token idea...
