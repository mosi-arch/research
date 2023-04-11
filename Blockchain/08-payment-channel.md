# How to build "payment channel" on Ethereum virtual machine (EVM):
## PART 1
- 1- create channel
- 2- require multi signature for create channel
- 3- closing channel automatically after found finish
- 4- closing channel after two signer accepting to close
- 5- create a factory contract for creating new channels

#### proof of payment 
"Hashed Timelock Contracts (HTLCs)" (hash timelock contract/transaction '[here](https://en.bitcoin.it/wiki/Hash_Time_Locked_Contracts)')

#### To build a payment channel on Ethereum, you can follow these steps:
- Create a smart contract for the payment channel.
- Implement multi-signature functionality to ensure secure channel creation.
- Set up automatic channel closing after the payment is complete.
- Allow for manual channel closing by requiring both signers to agree to close the channel.
- Optionally, create a factory contract to enable easy creation of new payment channels.

#### Now, write Smartcontract by using solidity
To create a payment channel on Ethereum using Solidity, you can follow these steps:
- Create a contract for the payment channel, which will include variables for the two parties involved, the balance of the channel, and the deadline for the channel to be closed.
- Implement a multi-signature requirement for creating the channel, which will ensure that both parties need to sign off on the creation of the channel.
- Use a time-based function to automatically close the channel if it has not been closed by the deadline.
- Implement a function that allows both parties to close the channel by signing a message with their private keys.
- Create a factory contract that can be used to create new payment channels.

Here's an example of what the Solidity code might look like:

```solidity
contract PaymentChannel {
    address payable public party1;
    address payable public party2;
    uint256 public balance;
    uint256 public deadline;

    constructor(address payable _party1, address payable _party2, uint256 _balance, uint256 _deadline) {
        party1 = _party1;
        party2 = _party2;
        balance = _balance;
        deadline = block.timestamp + _deadline;
    }

    receive() payable external {}
    fallback() payable external {}
    
    function createChannel() public {
        require(msg.sender == party1 || msg.sender == party2, "Only parties can create channel");
        require(balance == 0, "Channel already created");
        balance = address(this).balance;
    }
    
    function closeChannel() public {
        require(msg.sender == party1 || msg.sender == party2, "Only parties can close channel");
        require(block.timestamp >= deadline, "Channel not yet expired");
        // selfdestruct(party1); // selfdestruct deprecated
        (bool sent, ) = party1.call{value: address(this).balance}("");
        require(sent, "Failed to send Ether");
    }
    
    function closeChannelSigned(uint8 v, bytes32 r, bytes32 s, bytes32 hash) public {
        require(ecrecover(hash, v, r, s) != address(0), "Invalid signatures");
        // selfdestruct(party1); // selfdestruct deprecated
        (bool sent, ) = party1.call{value: address(this).balance}("");
        require(sent, "Failed to send Ether");
    }
    // ecrecover(hash, v, r, s); -> uint8 v, bytes32 r, bytes32 s, bytes32 hash

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }    
}
```

#### Factory
```solidity
contract PaymentChannelFactory {
    event ChannelCreated(address channel);

    function createChannel(address payable _party1, address payable _party2, uint256 _balance, uint256 _deadline) public {
        PaymentChannel channel = new PaymentChannel(_party1, _party2, _balance, _deadline);
        emit ChannelCreated(address(channel));
    }
}
```

### Disclaimer Note: 
that this is just an example implementation and you may need to modify it to suit your specific needs.

## PART 2
using "y combinator" for creating "payment channel" on ethereum. code in javascript\
*this is the unique code, never seen before around the  web!*

```JS
function YCombinator(func) {
    return (function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    })(function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    });
} 
// Create a payment channel on Ethereum
function createPaymentChannel(sender, receiver, amount) {
    return YCombinator(function(f) {
        return function(sender, receiver, amount) {
            // Create a new Ethereum account
            let account = web3.eth.accounts.create();
            // Send the amount from the sender to the new account
            web3.eth.sendTransaction({
                from: sender,
                to: account.address,
                value: amount
            });
            // Create a smart contract to manage the payment channel
            let contract = new web3.eth.Contract(paymentChannelABI);
            // Deploy the contract
            contract.deploy({
                data: paymentChannelBytecode,
                arguments: [sender, receiver, account.address]
            }).send({
                from: sender,
                gas: 1000000
            });
            // Return the address of the deployed contract
            return contract.options.address;
        };
    })(sender, receiver, amount);
}
```
#### Personal comment:
WHY USING **Y COMBINATOR FUNCTION PATTERN/PROGRAMMING**? function programming the true solution for blockchain programming, but some "idiot wealth seekers" love to waist time...\
More information about "Functional Programming" [here](https://github.com/mosi-arch/research/blob/main/Mathematics/04-lambda-recursion-function-programming.md) 
