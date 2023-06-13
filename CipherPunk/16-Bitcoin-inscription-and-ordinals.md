## Algorithm for adding an *inscription* to a *Bitcoin transaction*:

1. Create a new Bitcoin transaction using a library or API that provides access to the Bitcoin network. For example, you could use the `Transaction` class from the `bitcoinlib` library in Python.

2. Add inputs and outputs to the transaction as needed. Inputs typically reference previous transactions that have already sent Bitcoin to your address, while outputs specify the destination address and amount of Bitcoin to be sent.

3. Encode the inscription as needed. Inscriptions are typically added to the output script using an `OP_RETURN` opcode, which allows data to be added to the blockchain without affecting the Bitcoin transfer itself. Inscriptions can be in any format you choose, but they need to be encoded so they can be included in the script.

4. Add the inscription to the output script. Create a `Script` object with the `OP_RETURN` opcode and the encoded inscription, and add it to the output script for the transaction.

5. Sign the transaction with a private key. This step ensures that only you can authorize the transfer of Bitcoin from your address.

6. Broadcast the transaction to the Bitcoin network. Once the transaction is broadcast, it will be added to the blockchain and the inscription will be visible to anyone who views the transaction.

- How to add an inscription to a Bitcoin transaction using the `bitcoinlib` library:

```py
from bitcoinlib.transactions import Transaction, Script

# Create a new transaction
tx = Transaction()

# Add inputs and outputs to the transaction as needed
tx.add_input("prev_txid", "prev_output_index")
tx.add_output("dest_address", "amount")

# Add an inscription to the output script
inscription = "For goods and services"
script = Script(["OP_RETURN", inscription.encode("utf-8")])
tx.outputs[0].script = script

# Sign the transaction with a private key
tx.sign("private_key")

# Broadcast the transaction to the Bitcoin network
tx.broadcast()
```
- i can't run code, when write this article. but remember 2 years ago my freind show me some codes. i found this on our conversation archives.

**Brief summary**: adding an inscription to a Bitcoin transaction involves encoding additional information and adding it to the output script of the transaction using an `OP_RETURN` opcode. The inscription can be in any format and can provide additional context or metadata about the transaction. Ordinals, which refer to the position of a transaction within the blockchain, can be used in conjunction with inscriptions to provide a more complete picture of a transaction's place in the blockchain and its purpose. The process of adding an inscription to a Bitcoin transaction typically involves creating a new transaction, adding inputs and outputs, encoding the inscription, adding it to the output script, signing the transaction with a private key, and broadcasting the transaction to the Bitcoin network.

> @dev : google it [here](https://www.google.com/search?q=tell+more+about+ordinals+and+inscriptions%2C+by+example+code&rlz=1C1GCEA_enGB904GB904&ei=o1yIZKe0L5yrxc8PvJOEsAg&ved=0ahUKEwjnkci8m8D_AhWcVfEDHbwJAYYQ4dUDCA8&uact=5&oq=tell+more+about+ordinals+and+inscriptions%2C+by+example+code&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIICCEQoAEQwwQyCAghEKABEMMEOgoIABBHENYEELADOgoIIRCgARDDBBAKSgQIQRgAUM4IWLpzYIp6aAJwAXgAgAGBBogB3xGSAQM2LTOYAQCgAQHAAQHIAQg&sclient=gws-wiz-serp)

#### disclaimer:
This document has been made by my freind to show me the concept of **Bitcoin inscription** , in 2021.\
Actualy I hear in this month alot about this and **ordinals** , 
I as you know the miners in these past months build over a billion dollars from only users transactio. 
So I think again the **brc20** is another money game of miners. 
But this can help the ecosystem of BTC, and this is fantastic!
