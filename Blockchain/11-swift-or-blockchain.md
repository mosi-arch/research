## Swift or Blockchain, which-one is better?

The world of finance has undergone significant changes in recent years, with the rise of new technologies and payment systems. One of the most significant changes has been the emergence of blockchain-based payment systems, which offer a faster, cheaper, and more secure alternative to traditional payment systems like SWIFT.

SWIFT is a messaging system used by banks and financial institutions to securely and efficiently communicate information about financial transactions. SWIFT transactions involve multiple banks, with each bank sending and receiving messages to and from other banks. The transaction can take several days to complete, and there may be additional fees and charges involved. While SWIFT has been a reliable and trusted system for many years, it is not without its challenges. The system is slow, expensive, and prone to errors and delays. Additionally, the system is centralized, which means that there is a risk of fraud or hacking.

In contrast, blockchain-based payment systems offer a direct transfer of funds from the sender to the receiver, with no intermediaries involved. The transaction is processed almost immediately and the fees are typically lower compared to traditional payment systems. Blockchain-based payment systems are also more secure, as they use cryptographic algorithms to ensure the integrity and confidentiality of the transaction data. The decentralized nature of blockchain technology means that there is no single point of failure, which reduces the risk of fraud or hacking.

However, there are also some potential drawbacks to using blockchain-based payment systems. For example, there may be concerns about the stability and security of the underlying blockchain network, and there may be regulatory hurdles that need to be addressed. Additionally, the lack of intermediaries in blockchain-based payment systems means that there is less recourse for dispute resolution or error correction.

Overall, the choice between a traditional payment system like SWIFT and a blockchain-based payment system will depend on various factors, such as the specific needs of the parties involved and the regulatory environment in which the transaction takes place. While blockchain-based payment systems offer many advantages over traditional payment systems, they are not a panacea. It is important for businesses and financial institutions to carefully evaluate the benefits and drawbacks of each system and choose the one that is best suited for their needs.

#

### Looking these examples:

- Swift:
```python
sender_bic = "BANKAUS33XXXX"
receiver_bic = "BANKFRPPXXX"
intermediary_bic = "BANKGB2LXXX"
transaction_ref = "1234567890123456"
transaction_amount_usd = 100000
exchange_rate = 0.82
intermediary_fee_rate = 0.001

# Calculate transaction amounts
transaction_amount_local = transaction_amount_usd * exchange_rate
intermediary_fee = transaction_amount_usd * intermediary_fee_rate
transaction_amount_usd_total = transaction_amount_usd + intermediary_fee
transaction_amount_local_total = transaction_amount_usd_total * exchange_rate

# Format SWIFT message
swift_message = f"{{1:F01{sender_bic}0000000000}}{{2:I103{sender_bic}N}}{{3:{{108:MT103 {transaction_ref}}}}}" + \
                f"{{4:\n:20:{transaction_ref}\n:32A:210512USD{transaction_amount_usd_total:,.2f}\n" + \
                f":33B:EUR{transaction_amount_local_total:,.2f}\n:71A:OUR\n" + \
                f":71F:USD{intermediary_fee:,.2f}\n:71G/BEN/BENEFICIARY/ACCT-001\n" + \
                f":56A:{intermediary_bic}\n:57A:{receiver_bic}\n:50K:/1234567890\n" + \
                f"JOHN DOE\n123 MAIN STREET\nNEW YORK, NY 10001\nUSA\n:52A:{sender_bic}\n" + \
                f":59:/1234567891\nJANE DOE\n456 MAIN STREET\nLOS ANGELES, CA 90001\nUSA\n-}}"

print(swift_message)
```

- Output:
```js
{1:F01BANKAUS33XXXX0000000000}{2:I103BANKAUS33XXXXN}{3:{108:MT103 1234567890123456}}{4:
:20:1234567890123456
:32A:210512USD100,100.00
:33B:EUR82,082.00
:71A:OUR
:71F:USD100.00
:71G/BEN/BENEFICIARY/ACCT-001
:56A:BANKGB2LXXX
:57A:BANKFRPPXXX
:50K:/1234567890
JOHN DOE
123 MAIN STREET
NEW YORK, NY 10001
USA
:52A:BANKAUS33XXXX
:59:/1234567891
JANE DOE
456 MAIN STREET
LOS ANGELES, CA 90001
USA
-}
```

- Blockchain:
```python
sender_address = "0x1234567890abcdef"
receiver_address = "0x0987654321fedcba"
transaction_amount = 100000
transaction_fee = 0.01

# Calculate total transaction amount
total_amount = transaction_amount * (1 + transaction_fee)

# Format blockchain transaction
blockchain_transaction = f"From: {sender_address}\nTo: {receiver_address}\nAmount: {transaction_amount}\n" + \
                         f"Transaction Fee: {transaction_fee}\nTotal Amount: {total_amount}"

print(blockchain_transaction)
```

- Output:
```js
From: 0x1234567890abcdef
To: 0x0987654321fedcba
Amount: 100000
Transaction Fee: 0.01
Total Amount: 101000.0
```

