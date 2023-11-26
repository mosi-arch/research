formula asap

---

**AMM** -> Automated Market Maker
- notice: in central-financial market, automation different by dex-gen2. because dex-gen2 using "pool" for creating the value/volume.
```js
x * y = k
k -> always constant (uniswap k is 0)
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
- - this codes simple, not for product, for learning.
- this codes have "address(x)", this is for test and codes have error.

#

- CMMM [example](https://github.com/mosi-arch/research/blob/main/Blockchain/01-dex-methodology.md#cmmm)
- CFMM [example](https://github.com/mosi-arch/research/blob/main/Blockchain/01-dex-methodology.md#cfmm)
- CPMM [example](https://github.com/mosi-arch/research/blob/main/Blockchain/01-dex-methodology.md#cpmm)
- CSMM [example](https://github.com/mosi-arch/research/blob/main/Blockchain/01-dex-methodology.md#csmm)

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

#### CFMM

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract CFMMExchange {
    
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowed;
    
    uint256 public totalSupply;
    string public name;
    string public symbol;
    uint8 public decimals;
    
    uint256 public reserve0;
    uint256 public reserve1;
    uint256 public kLast;
    
    uint256 private constant MAX_UINT256 = type(uint256).max;
    
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Sync(uint256 reserve0, uint256 reserve1);
    
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _reserve0, uint256 _reserve1) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        reserve0 = _reserve0;
        reserve1 = _reserve1;
        kLast = _reserve0 * _reserve1; // Initialize kLast to the initial product of the reserves
    }
    
    function mint(address account, uint256 amount) public {
        require(amount > 0, "Amount must be greater than zero");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 amount0 = amount * balance0 / totalSupply;
        uint256 amount1 = amount * balance1 / totalSupply;
        require(amount0 > 0 && amount1 > 0, "Invalid amount");
        balances[account] += amount;
        totalSupply += amount;
        reserve0 += amount0;
        reserve1 += amount1;
        emit Transfer(address(0), account, amount);
        emit Sync(reserve0, reserve1);
    }
    
    function burn(address account, uint256 amount) public {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[account] >= amount, "Insufficient balance");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 amount0 = amount * balance0 / totalSupply;
        uint256 amount1 = amount * balance1 / totalSupply;
        require(amount0 > 0 && amount1 > 0, "Invalid amount");
        balances[account] -= amount;
        totalSupply -= amount;
        reserve0 -= amount0;
        reserve1 -= amount1;
        emit Transfer(account, address(0), amount);
        emit Sync(reserve0, reserve1);
    }
    
    function swap(uint256 amountIn, uint256 amountOut, address to) public {
        require(amountIn > 0 && amountOut > 0, "Invalid amount");
        require(to != address(0) && to != address(this), "Invalid recipient");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 amountInWithFee = amountIn * 997;
        uint256 numerator = amountInWithFee * balance1;
        uint256 denominator = balance0 * 1000 + amountInWithFee;
        uint256 amountOutWithFee = numerator / denominator;
        require(amountOutWithFee <= amountOut, "Insufficient output amount");
        balances[address(0)] += amountIn;
        balances[address(1)] -= amountOutWithFee;
        balances[to] += amountOut;
        emit Transfer(address(0), to, amountOut);
        emit Sync(reserve0, reserve1);
    }
    
    function setReserves(uint256 _reserve0, uint256 _reserve1) public {
        require(msg.sender == address(this), "Only the contract owner can set reserves");
        require(_reserve0 > 0 && _reserve1 > 0, "Reserves must be greater than zero");
        reserve0 = _reserve0;
        reserve1 = _reserve1;
        kLast = reserve0 * reserve1;
        emit Sync(reserve0, reserve1);
    }
    
    function skim(address to) public {
        require(to != address(0) && to != address(this), "Invalid recipient");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 skimAmount0 = balance0 - reserve0;
        uint256 skimAmount1 = balance1 - reserve1;
        balances[address(0)] -= skimAmount0;
        balances[address(1)] -= skimAmount1;
        balances[to] += skimAmount0;
        balances[to] += skimAmount1;
        emit Transfer(address(0), to, skimAmount0 + skimAmount1);
        emit Sync(reserve0, reserve1);
    }
    
    function sync() public {
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 product = balance0 * balance1;
        if (product > 0 && product >= kLast * 2) {
            uint256 rootK = sqrt(product);
            uint256 amount0 = rootK - reserve0;
            uint256 amount1 = rootK - reserve1;
            require(amount0 > 0 && amount1 > 0, "Invalid amount");
            balances[address(0)] += amount0;
            balances[address(1)] += amount1;
            balances[address(0)] -= amount0;
            balances[address(1)] -= amount1;
            reserve0 = rootK;
            reserve1 = rootK;
            kLast = rootK * rootK;
            emit Sync(reserve0, reserve1);
        }
    }
    
    function sqrt(uint256 x) private pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
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
}
```

```js
const Web3 = require('web3');
const abi = [ // ABI of the CFMMExchange contract
    // TODO: add ABI here
];

const web3 = new Web3('http://localhost:8545'); // create a Web3 instance pointing to your local Ethereum node
const contractAddress = '0x1234567890123456789012345678901234567890'; // replace with the address of your deployed contract
const cfmmExchange = new web3.eth.Contract(abi, contractAddress); // create a contract instance

// Example usage: swap some tokens
const amountIn = 100; // replace with the amount of tokens to swap in
const amountOut = 200; // replace with the expected amount of tokens to receive
const recipientAddress = '0x1234567890123456789012345678901234567891'; // replace with the address of the recipient

cfmmExchange.methods.swap(amountIn, amountOut, recipientAddress).send({ from: web3.eth.defaultAccount })
.then(() => {
    console.log(`${amountIn} tokens swapped for ${amountOut} tokens and sent to ${recipientAddress}`);
})
.catch((error) => {
    console.error(error);
});
```


#### CPMM

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract CPMMExchange {
    
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowed;
    
    uint256 public totalSupply;
    string public name;
    string public symbol;
    uint8 public decimals;
    
    uint256 public reserve0;
    uint256 public reserve1;
    
    uint256 private constant MAX_UINT256 = type(uint256).max;
    
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Sync(uint256 reserve0, uint256 reserve1);
    
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _reserve0, uint256 _reserve1) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        reserve0 = _reserve0;
        reserve1 = _reserve1;
        totalSupply = sqrt(reserve0 * reserve1); // Initialize total supply to the square root of the product of the reserves
    }
    
    function mint(address account, uint256 amount) public {
        require(amount > 0, "Amount must be greater than zero");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 amount0 = amount * balance0 / totalSupply;
        uint256 amount1 = amount * balance1 / totalSupply;
        require(amount0 > 0 && amount1 > 0, "Invalid amount");
        balances[account] += amount;
        totalSupply += amount;
        reserve0 += amount0;
        reserve1 += amount1;
        emit Transfer(address(0), account, amount);
        emit Sync(reserve0, reserve1);
    }
    
    function burn(address account, uint256 amount) public {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[account] >= amount, "Insufficient balance");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 amount0 = amount * balance0 / totalSupply;
        uint256 amount1 = amount * balance1 / totalSupply;
        require(amount0 > 0 && amount1 > 0, "Invalid amount");
        balances[account] -= amount;
        totalSupply -= amount;
        reserve0 -= amount0;
        reserve1 -= amount1;
        emit Transfer(account, address(0), amount);
        emit Sync(reserve0, reserve1);
    }
    
    function swap(uint256 amountIn, uint256 amountOut, address to) public {
        require(amountIn > 0 && amountOut > 0, "Invalid amount");
        require(to != address(0) && to != address(this), "Invalid recipient");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 amountInWithFee = amountIn * 997;
        uint256 numerator = amountInWithFee * balance1;
        uint256 denominator = balance0 * 1000 + amountInWithFee;
        uint256 amountOutWithFee = numerator / denominator;
        require(amountOutWithFee <= amountOut, "Insufficient output amount");
        balances[address(0)] += amountIn;
        balances[address(1)] -= amountOutWithFee;
        balances[to] += amountOut;
        emit Transfer(address(0), to, amountOut);
        emit Sync(reserve0, reserve1);
    }
    
    function setReserves(uint256 _reserve0, uint256 _reserve1) public {
        require(msg.sender == address(this), "Only the contract owner can set reserves");
        require(_reserve0 > 0 && _reserve1 > 0, "Reserves must be greater than zero");
        reserve0 = _reserve0;
        reserve1 = _reserve1;
        totalSupply = sqrt(reserve0 * reserve1);
        emit Sync(reserve0, reserve1);
    }
    
    function skim(address to) public {
        require(to != address(0) && to != address(this), "Invalid recipient");
        uint256 balance0 = balances[address(0)];
        uint256 balance1 = balances[address(1)];
        uint256 skimAmount0 = balance0 - reserve0;
        uint256 skimAmount1 = balance1 - reserve1;
        balances[address(0)] -= skimAmount0;
        balances[address(1)] -= skimAmount1;
        balances[to] += skimAmount0;
        balances[to] += skimAmount1;
        emit Transfer(address(0), to, skimAmount0 + skimAmount1);
        emit Sync(reserve0, reserve1);
    }
    
    function transfer(address to, uint256 value) public returns (bool) {
        require(to != address(0) && to != address(this), "Invalid recipient");
        require(balances[msg.sender] >= value, "Insufficient balance");
        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }
    
    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        require(from != address(0) && from != address(this), "Invalid sender");
        require(to != address(0) && to != address(this), "Invalid recipient");
        require(balances[from] >= value, "Insufficient balance");
        require(allowed[from][msg.sender] >= value, "Not enough allowance");
        balances[from] -= value;
        balances[to] += value;
        allowed[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }
    
    function approve(address spender, uint256 value) public returns (bool) {
        require(spender != address(0) && spender != address(this), "Invalid spender");
        allowed[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }
    
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowed[owner][spender];
    }
    
    function sqrt(uint256 x) private pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }
    
}
```

```js
const Web3 = require('web3');
const contractAbi = [ /* ABI goes here */ ];
const contractAddress = '/* Contract address goes here */';

const web3 = new Web3('/* Provider URL goes here */');
const contract = new web3.eth.Contract(contractAbi, contractAddress);

async function getBalances() {
    const [balance0, balance1] = await Promise.all([
        contract.methods.balances('/* Address of token 0 goes here */').call(),
        contract.methods.balances('/* Address of token 1 goes here */').call()
    ]);
    return [balance0, balance1];
}

async function getReserves() {
    const [reserve0, reserve1] = await Promise.all([
        contract.methods.reserve0().call(),
        contract.methods.reserve1().call()
    ]);
    return [reserve0, reserve1];
}

async function getTotalSupply() {
    return await contract.methods.totalSupply().call();
}

async function getTokenInfo() {
    const [name, symbol, decimals] = await Promise.all([
        contract.methods.name().call(),
        contract.methods.symbol().call(),
        contract.methods.decimals().call()
    ]);
    return [name, symbol, decimals];
}

async function mint(amount) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.mint(accounts[0], amount).send({ from: accounts[0] });
}

async function burn(amount) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.burn(accounts[0], amount).send({ from: accounts[0] });
}

async function swap(amountIn, amountOut, to) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.swap(amountIn, amountOut, to).send({ from: accounts[0] });
}

async function setReserves(reserve0, reserve1) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.setReserves(reserve0, reserve1).send({ from: accounts[0] });
}

async function skim(to) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.skim(to).send({ from: accounts[0] });
}

async function transfer(to, amount) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.transfer(to, amount).send({ from: accounts[0] });
}

async function transferFrom(from, to, amount) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.transferFrom(from, to, amount).send({ from: accounts[0] });
}

async function approve(spender, amount) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.approve(spender, amount).send({ from: accounts[0] });
}

async function getAllowance(owner, spender) {
    return await contract.methods.allowance(owner, spender).call();
}
```


#### CSMM

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CSMM {
    struct Token {
        uint256 reserve;
        uint256 supply;
    }
    
    mapping(address => Token) public tokens;
    
    event TokensAdded(address indexed token1, uint256 amount1, address indexed token2, uint256 amount2);
    event TokensRemoved(address indexed token1, uint256 amount1, address indexed token2, uint256 amount2);
    
    function addTokens(address token1, uint256 amount1, address token2, uint256 amount2) external {
        require(amount1 > 0 && amount2 > 0, "Amounts must be greater than zero");
        tokens[token1].reserve += amount1;
        tokens[token1].supply += amount1;
        tokens[token2].reserve += amount2;
        tokens[token2].supply += amount2;
        emit TokensAdded(token1, amount1, token2, amount2);
    }
    
    function removeTokens(address token1, uint256 amount1, address token2, uint256 amount2) external {
        require(amount1 > 0 && amount2 > 0, "Amounts must be greater than zero");
        require(tokens[token1].supply >= amount1 && tokens[token2].supply >= amount2, "Insufficient reserves");
        tokens[token1].reserve -= amount1;
        tokens[token1].supply -= amount1;
        tokens[token2].reserve -= amount2;
        tokens[token2].supply -= amount2;
        emit TokensRemoved(token1, amount1, token2, amount2);
    }
    
    function getConstant(address token1, address token2) external view returns (uint256) {
        require(tokens[token1].supply > 0 && tokens[token2].supply > 0, "Tokens not found");
        return tokens[token1].reserve * tokens[token2].reserve;
    }
}
```

```js
const Web3 = require('web3');
const CSMMabi = require('./CSMMabi.json');

const web3 = new Web3('http://localhost:8545');
const CSMMaddress = '0x1234567890123456789012345678901234567890';
const CSMM = new web3.eth.Contract(CSMMabi, CSMMaddress);

const token1 = '0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const token2 = '0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb';

// Add tokens to the DEX
const addTokens = async (token1Amount, token2Amount) => {
  const accounts = await web3.eth.getAccounts();
  const result = await CSMM.methods.addTokens(token1, token1Amount, token2, token2Amount).send({ from: accounts[0] });
  console.log(result);
};

// Remove tokens from the DEX
const removeTokens = async (token1Amount, token2Amount) => {
  const accounts = await web3.eth.getAccounts();
  const result = await CSMM.methods.removeTokens(token1, token1Amount, token2, token2Amount).send({ from: accounts[0] });
  console.log(result);
};

// Get the constant of the CSMM formula
const getConstant = async () => {
  const result = await CSMM.methods.getConstant(token1, token2).call();
  console.log(result);
};
```
