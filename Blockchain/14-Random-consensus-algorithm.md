## Simulate Random Consensus Algorithm
A high-level simulation of how a blockchain network, validation, and transaction process might work.\
Simple example of 10 validator, 1 random validate, second random valid the block and confirm the first validator, other validator accept the block to save in DLT.

**1. Creating the Blockchain Network**:
To create a blockchain network, we need to first define the rules of the network, such as the consensus algorithm, the block size, and the reward for mining a block. We then create a genesis block, which is the first block in the chain and contains all the rules of the network. Once the genesis block is created, nodes can join the network and start validating and mining blocks.

**2. Validation**:
Nodes in a blockchain network validate transactions by checking if they meet the rules of the network. For example, if the network has a rule that a transaction must have a valid digital signature, nodes will check if the signature is valid. If a transaction is valid, nodes will broadcast it to the network.

**3. Mining**:
Mining is the process of adding transactions to the blockchain by creating a new block. Miners compete to create a new block by solving a complex mathematical puzzle, which requires a lot of computational power. The first miner to solve the puzzle creates a new block and broadcasts it to the network.

**4. Block Confirmation**:
Once a block is created, it needs to be confirmed by other nodes in the network. Nodes will check if the block contains valid transactions and meets the rules of the network. If the block is valid, nodes will add it to their copy of the blockchain, creating a new version of the blockchain.

**5. Transaction Process**:
To process a transaction, a user sends a transaction to the network, which is then validated by nodes. Once the transaction is validated, miners include it in the next block they create. Once the block is confirmed by the network, the transaction is considered complete.

**P.S**: Blockchain networks use consensus algorithms to validate transactions and create new blocks. Miners compete to create new blocks, which are then confirmed by other nodes in the network. Transactions are processed by sending them to the network for validation, inclusion in a block, and confirmation.

#

The key steps in a blockchain network, including transaction processing, validation, and mining:

| Step | Description |
| --- | --- |
| **Step 1: Define Rules** | Define the rules of the blockchain network, including the consensus algorithm, block size, and reward for mining a block. |
| **Step 2: Create Genesis Block** | Create the first block in the chain, which contains all the rules of the network. |
| **Step 3: Join Network** | Nodes join the network and start validating and mining blocks. |
| **Step 4: Validate Transaction** | Nodes validate transactions by checking if they meet the rules of the network. |
| **Step 5: Broadcast Transaction** | If a transaction is valid, nodes broadcast it to the network. |
| **Step 6: Mine Block** | Miners compete to create a new block by solving a complex mathematical puzzle. |
| **Step 7: Create Block** | The first miner to solve the puzzle creates a new block and broadcasts it to the network. |
| **Step 8: Confirm Block** | Nodes confirm the block by checking if it contains valid transactions and meets the rules of the network. |
| **Step 9: Add Block to Blockchain** | If the block is valid, nodes add it to their copy of the blockchain, creating a new version of the blockchain. |
| **Step 10: Process Transaction** | To process a transaction, a user sends a transaction to the network for validation, inclusion in a block, and confirmation. |

#

### How to validate randomly:
How a validation system might work in a blockchain network using a random chance method.

Let's say we have a network with 10 nodes, and each node has an equal chance of being selected as a validator for a particular block. When a block is created, one of the nodes is randomly selected to validate the block.

The validator checks the block to ensure that it meets the rules of the network. If the block is valid, the validator broadcasts the block to the other nodes in the network. The other nodes receive the block and check if it has been validated by a trusted validator. If the block has been validated, the other nodes accept the validation and add the block to their copy of the blockchain.

If the validator finds that the block is invalid, they reject the block and do not broadcast it to the network. The other nodes do not receive the block and do not add it to their copy of the blockchain.

In this system, each node has an equal chance of being selected as a validator for each block, which ensures that no single node has too much power or influence over the network. The random chance method also makes it difficult for attackers to predict which node will be selected as a validator, which makes the network more secure.

#

### Tree Chart:

```
Validation Process
├── A block is created
├── A validator is randomly selected from the network
│   ├── Validator checks the block
│   │   ├── If block is valid
│   │   │   ├── Validator broadcasts block to the network
│   │   │   └── Other nodes accept validation and add block to their copy of the blockchain
│   │   └── If block is invalid
│   │       └── Validator rejects block and does not broadcast it to the network
│   └── Other nodes receive block and check if it has been validated by a trusted validator
│       ├── If block has been validated
│       │   └── Other nodes accept validation and add block to their copy of the blockchain
│       └── If block has not been validated
│           └── Other nodes do not accept validation and do not add block to their copy of the blockchain
└── Process repeats for each new block created in the network
```

#

### Python example - 1:
The first validator valid, Second valid too, then all other accept.
```py
import random

# Define the network of nodes
nodes = ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5', 'Node 6', 'Node 7', 'Node 8', 'Node 9', 'Node 10']

# Define the validation function
def validate_block(block, validator):
    # Check if block is valid
    if block.is_valid():
        print(f'{validator} validated the block.')
        return True
    else:
        print(f'{validator} rejected the block.')
        return False

# Create a block
class Block:
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        # Define rules for a valid block
        if len(self.data) > 0:
            return True
        else:
            return False

# Simulate the validation process
block = Block('Transaction data')
validator = random.choice(nodes)
print(f'{validator} was selected as the validator for the block.')
if validate_block(block, validator):
    # Broadcast block to other nodes
    for node in nodes:
        if node != validator:
            print(f'Block broadcasted to {node}.')
else:
    # Block is invalid, do not broadcast
    print('Block was not broadcasted due to invalidity.')
```

#

### Python example - 2:
The second validator validating block then confirm first validator, then broadcasing to other validator for accept.
```py 
import random

# Define the network of nodes
nodes = ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5', 'Node 6', 'Node 7', 'Node 8', 'Node 9', 'Node 10']

# Define the validation function
def validate_block(block, validator):
    # Check if block is valid
    if block.is_valid():
        print(f'{validator} validated the block.')
        return True
    else:
        print(f'{validator} rejected the block.')
        return False

# Define the second validation function
def validate_validator(block, validator, second_validator):
    # Check if first validator is trusted
    if validate_block(block, validator):
        # Check if second validator is also trusted
        if validate_block(block, second_validator):
            print(f'{second_validator} validated {validator}.')
            return True
        else:
            print(f'{second_validator} rejected {validator}.')
            return False
    else:
        print(f'{second_validator} rejected {validator} due to invalidity.')
        return False

# Create a block
class Block:
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        # Define rules for a valid block
        if len(self.data) > 0:
            return True
        else:
            return False

# Simulate the validation process
block = Block('Transaction data')
validator = random.choice(nodes)
second_validator = random.choice([node for node in nodes if node != validator])
print(f'{validator} was selected as the first validator and {second_validator} was selected as the second validator.')
if validate_validator(block, validator, second_validator):
    # Broadcast block to other nodes
    for node in nodes:
        if node not in [validator, second_validator]:
            print(f'Block broadcasted to {node}.')
else:
    # Block is invalid or not validated, do not broadcast
    print('Block was not broadcasted due to invalidity or lack of validation.')
```

Final step, looking the tree chart of this code:
```
Validation Process
├── A block is created
├── Two validators are randomly selected from the network
│   ├── Validator 1 checks the block
│   │   ├── If block is valid
│   │   │   ├── Validator 1 broadcasts block to Validator 2
│   │   │   └── Validator 2 validates Validator 1's validation
│   │   │       ├── If Validator 2 validates Validator 1
│   │   │       │   ├── Validator 2 broadcasts block to the network
│   │   │       │   └── Other nodes accept validation and add block to their copy of the blockchain
│   │   │       └── If Validator 2 rejects Validator 1
│   │   │           └── Block is not broadcasted
│   │   └── If block is invalid
│   │       └── Block is not broadcasted
│   └── Validator 2 receives block and validates Validator 1's validation
│       ├── If Validator 2 validates Validator 1
│       │   ├── Validator 2 broadcasts block to the network
│       │   └── Other nodes accept validation and add block to their copy of the blockchain
│       └── If Validator 2 rejects Validator 1
│           └── Block is not broadcasted
└── Process repeats for each new block created in the network
```
