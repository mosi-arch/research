formula asap

---

**AMM** -> Automated Market Maker
- notice: in central-financial market, automation different by dex-gen2. because dex-gen2 using "pool" for creating the volue/volum.
```js
x * y = k
k -> always constant
x -> token a
y -> token b
```

- **Market maker with constant averages**\
Constant manage with market maker (**CMMM**)\
*CMMM* -> There is no exchange fee
- **Market maker with consistent performance**\
Constant function market maker (**CFMM**)\
*CFMM* -> Use on secondary markets & arbitrage
- **Market maker with a fixed product**\
Constant product with market maker (**CPMM**)\
*CPMM* -> "k" incressing by dex (The exchange fee is added to the storage pool)
- **Market maker with fixed totals**\
Constant summary with market maker (**CSMM**)\
*CSMM* -> Not good for dex strategies. Arbitrageurs can empty the reserve pool

#

## Farsi:
بازارساز خودکار\
بازارسازان با میانگین ثابت\
بازارسازان با عملکرد ثابت\
بازارسازان با محصول ثابت\
بازارسازان با مجموع ثابت

---

### Simple codes:
- don't use theses codes on product, these codes just example.

#### CMMM
```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract CMMMExchange {
    
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowed;
    mapping(address => bool) public marketMaker;
    
    uint256 public totalSupply;
    string public name;
    string public symbol;
    uint8 public decimals;
    
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    constructor(string memory _name, string memory _symbol, uint8 _decimals) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
    }
    
    function mint(address account, uint256 amount) public {
        require(marketMaker[msg.sender], "Only market makers can mint tokens");
        totalSupply += amount;
        balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }
    
    function burn(address account, uint256 amount) public {
        require(marketMaker[msg.sender], "Only market makers can burn tokens");
        require(balances[account] >= amount, "Insufficient balance");
        totalSupply -= amount;
        balances[account] -= amount;
        emit Transfer(account, address(0), amount);
    }
    
    function transfer(address to, uint256 value) public returns (bool) {
        require(balances[msg.sender] >= value, "Insufficient balance");
        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }
    
    function approve(address spender, uint256 value) public returns (bool) {
        allowed[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }
    
    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        require(balances[from] >= value, "Insufficient balance");
        require(allowed[from][msg.sender] >= value, "Not authorized to transfer this amount");
        balances[from] -= value;
        balances[to] += value;
        allowed[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }
    
    function setMarketMaker(address account, bool isMarketMaker) public {
        require(msg.sender == address(this), "Only the contract owner can set market maker status");
        marketMaker[account] = isMarketMaker;
    }
}
```

```js
const Web3 = require('web3');
const abi = [ // ABI of the CMMMExchange contract
    // TODO: add ABI here
];

const web3 = new Web3('http://localhost:8545'); // create a Web3 instance pointing to your local Ethereum node
const contractAddress = '0x1234567890123456789012345678901234567890'; // replace with the address of your deployed contract
const cmmmExchange = new web3.eth.Contract(abi, contractAddress); // create a contract instance

// Example usage: mint some tokens
const marketMakerAddress = '0x1234567890123456789012345678901234567891'; // replace with the address of a market maker
const recipientAddress = '0x1234567890123456789012345678901234567892'; // replace with the address of the recipient
const amountToMint = 100; // replace with the amount of tokens to mint

cmmmExchange.methods.setMarketMaker(marketMakerAddress, true).send({ from: web3.eth.defaultAccount })
.then(() => {
    return cmmmExchange.methods.mint(recipientAddress, amountToMint).send({ from: marketMakerAddress });
})
.then(() => {
    console.log(`${amountToMint} tokens minted and sent to ${recipientAddress}`);
})
.catch((error) => {
    console.error(error);
});
```
