## ElGamal Encryption
ElGamal encryption is a public-key encryption scheme that was first proposed by Taher Elgamal in 1985. It is based on the computational difficulty of the discrete logarithm problem in a finite field. The scheme is named after its inventor, Taher Elgamal.

The ElGamal encryption scheme has two parts: key generation and encryption/decryption. The key generation algorithm generates a public key and a private key. The encryption algorithm takes a plaintext message and the recipient's public key as input and produces a ciphertext. The decryption algorithm takes the ciphertext and the recipient's private key as input and produces the plaintext message.

Mathematics of the ElGamal encryption scheme:

Key Generation:
- 1.Choose a large prime number p.
- 2.Choose a primitive root g modulo p.
- 3.Choose a random integer x such that 1 <= x <= p-2.
- 4.Compute y = g^x mod p.
- 5.The public key is (p, g, y). The private key is x.

Encryption:
- 1.Choose a random integer k such that 1 <= k <= p-2 and gcd(k, p-1) = 1.
- 2.Compute c1 = g^k mod p.
- 3.Compute c2 = m * y^k mod p, where m is the plaintext message.
- 4.The ciphertext is (c1, c2).

Decryption:
- 1.Compute s = c1^x mod p.
- 2.Compute the plaintext message as m = c2 * s^(-1) mod p, where s^(-1) is the modular multiplicative inverse of s modulo p.

The "ElGamal encryption scheme" uses the properties of modular arithmetic and discrete logarithms to provide secure public-key encryption. The scheme is based on the difficulty of computing discrete logarithms, which is believed to be a hard problem in certain mathematical groups. The security of the scheme depends on the choice of the prime number p and the random values used for encryption.

---

### A Game Scenario:
- a dice game by two players
- using "ElGamal encryption" for not reveal data from two players to others
- then if a player dice equal 6 and other less then 6, then 6 won all bet
- each round they start drop dice, a bet on the table, if anyone won then table 0 znd bet send to winner

#### mathematics formula

=====================================

define variables:

- p: a large prime number
- g: a primitive root modulo p
- x1, x2: private keys of Player 1 and Player 2 respectively
- y1 = g^x1 mod p, y2 = g^x2 mod p: public keys of Player 1 and Player 2 respectively
- m: the bet amount
- r: a random number chosen by Player 1

game logic (simple random generator, not safe):

- 1.Player 1 chooses a random number r and calculates c1 = g^r mod p and c2 = (y2^r * 6) mod p.
- 2.Player 1 sends c1 and c2 to Player 2.
- 3.Player 2 calculates s = c1^x2 mod p and recovers the plaintext by dividing c2 by s: m' = c2 / s mod p = (y2^r * 6 * s^(-1)) mod p.
- 4.Player 2 drops the dice and determines the outcome d, where 1 <= d <= 6.
- 5.If d < 6, Player 2 bets m' on the table and sends the bet to Player 1. If d = 6, Player 2 bets 0 on the table and sends the entire amount m' to Player 1.
- 6.Player 1 drops the dice and determines the outcome e, where 1 <= e <= 6.
- 7.If e < 6, Player 1 bets m' on the table and sends the bet to Player 2. If e = 6, Player 1 bets 0 on the table and sends the entire amount m' to Player 2.

To determine the winner of each round, we compare the outcomes of the two dice rolls. If one player rolls a 6 and the other rolls less than 6, the player who rolled a 6 wins the entire bet on the table.

In mathematical notation, the above steps can be represented as follows:

Step 1:
- c1 = g^r mod p
- c2 = (y2^r * 6) mod p

Step 3:
- s = c1^x2 mod p
- m' = (c2 * s^(-1)) mod p = (y2^r * 6 * s^(-1)) mod p

Step 5:
- if d < 6: Player 2 bets m' on the table and sends the bet to Player 1
- if d = 6: Player 2 bets 0 on the table and sends the entire amount m' to Player 1

Step 7:
- if e < 6: Player 1 bets m' on the table and sends the bet to Player 2
- if e = 6: Player 1 bets 0 on the table and sends the entire amount m' to Player 2

The "ElGamal encryption scheme" is used to encrypt the bet amount and the outcome of one player's dice roll (multiplied by 6). The other player then decrypts the message and places a bet on the table based on their own dice roll. The winner of each round is determined by comparing the two dice rolls, with the possibility of one player winning the entire bet if they roll a 6 and the other player does not.

#### Python example:

=====================================

Python simple example (not use in product, teaching purposes):\
need to ensure the security of the communication channel and properly handle potential errors and exceptions.\
use pycryptodome library for ElGamal encryption.

```py
from Crypto.Util.number import getPrime, getRandomRange, inverse
from Crypto.PublicKey import ElGamal

# Generate a large prime number p and a primitive root g modulo p
p = getPrime(512)
g = 2
while pow(g, (p-1)//2, p) != 1:
    g += 1

# Generate private keys and public keys for Player 1 and Player 2
x1 = getRandomRange(1, p-1)
x2 = getRandomRange(1, p-1)
y1 = pow(g, x1, p)
y2 = pow(g, x2, p)

# Initialize the ElGamal objects for encryption and decryption
elgamal1 = ElGamal.generate(512)
elgamal2 = ElGamal.generate(512)

# Player 1 chooses a random number r and encrypts the bet amount and their dice roll
r = getRandomRange(1, p-1)
bet = 10  # example bet amount
dice1 = 6  # example dice roll
ciphertext1 = elgamal1.encrypt(str(bet) + ',' + str(dice1*6), r, y2)

# Player 1 sends the ciphertext to Player 2
ciphertext_bytes = ciphertext1[0].to_bytes() + ciphertext1[1].to_bytes()
ciphertext2 = (int.from_bytes(ciphertext_bytes, byteorder='big'),)

# Player 2 decrypts the ciphertext and determines their own dice roll
plaintext_bytes = elgamal2.decrypt(ciphertext2).split(b',')
bet2 = int.from_bytes(plaintext_bytes[0], byteorder='big')
dice2 = int.from_bytes(plaintext_bytes[1], byteorder='big') // 6

# Determine the outcome of the game and transfer the bet amount accordingly
if dice1 > dice2:
    print("Player 1 wins!")
    if dice1 == 6:
        transfer_amount = bet2 + bet
    else:
        transfer_amount = bet
    print("Transfer amount: ", transfer_amount)
else:
    print("Player 2 wins!")
    if dice2 == 6:
        transfer_amount = bet2 + bet
    else:
        transfer_amount = bet
    print("Transfer amount: ", transfer_amount)
```

#### Solidity Example:

=====================================

solidity simple example (i made couple bug in code, to not usable. so please dont use this):\
random generators is simple and not safe in this example.\
solidity not good language for simulating a game, this is example.\
"block.prevrandao" is new in solidity, generate random from bacon chain.

```solidity 
pragma solidity 0.8;

contract DiceGame {
    uint256 constant public p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f; // large prime number
    uint256 constant public g = 2; // primitive root modulo p
    
    struct Player {
        uint256 privateKey;
        uint256 publicKey;
        uint256 diceRoll;
        uint256 bet;
        uint256 winnings;
    }
    
    Player public player1;
    Player public player2;
    bool public gameEnded;
    address public winner;
    
    function joinGame() public payable {
        require(msg.value > 0, "Bet amount must be greater than zero.");
        require(player1.publicKey == 0 || player2.publicKey == 0, "Game is already full.");
        
        if (player1.publicKey == 0) {
            player1.privateKey = uint256(keccak256(abi.encodePacked(msg.sender, block.prevrandao)));
            player1.publicKey = powMod(g, player1.privateKey, p);
            player1.bet = msg.value;
        } else {
            player2.privateKey = uint256(keccak256(abi.encodePacked(msg.sender, block.prevrandao)));
            player2.publicKey = powMod(g, player2.privateKey, p);
            player2.bet = msg.value;
        }
    }
    
    function playGame(uint256 diceRoll) public {
        require(player1.publicKey != 0 && player2.publicKey != 0, "Game is not full yet.");
        require(msg.sender == winner || winner == address(0), "Game has already ended.");
        require(diceRoll >= 1 && diceRoll <= 6, "Dice roll must be between 1 and 6.");
        
        if (msg.sender == address(this)) {
            // Game is being resumed after encryption
            uint256 plaintext1 = decrypt(player1.privateKey, player2.publicKey, player1.diceRoll);
            uint256 plaintext2 = decrypt(player2.privateKey, player1.publicKey, player2.diceRoll);
            uint256 sum = plaintext1 + plaintext2;
            if (sum == 6 || (player1.diceRoll == 6 && player2.diceRoll < 6) || (player2.diceRoll == 6 && player1.diceRoll < 6)) {
                // Player with the highest dice roll or a roll of 6 wins the bet
                winner = (player1.diceRoll > player2.diceRoll) ? payable(msg.sender) : (player2.diceRoll > player1.diceRoll) ? payable(address(this)) : address(0);
                if (winner != address(0)) {
                    winner.transfer(player1.winnings + player2.winnings);
                }
            }
            gameEnded = true;
        } else {
            // Player rolls the dice and encrypts the result
            uint256 r = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp, block.difficulty)));
            player1.diceRoll = diceRoll;
            player2.diceRoll = getRandomDiceRoll(r);
            uint256 ciphertext1 = encrypt(player1.publicKey, player2.privateKey, player1.diceRoll * 6 + player1.bet);
            uint256 ciphertext2 = encrypt(player2.publicKey, player1.privateKey, player2.diceRoll * 6 + player2.bet);
            player1.bet = 0;
            player2.bet = 0;
            player1.winnings = 0;
            player2.winnings = 0;
            winner = address(this);
            gameEnded = false;
            emit GameStarted(ciphertext1, ciphertext2);
        }
    }
    
    function powMod(uint256 base, uint256 exponent, uint256 modulus) internal pure returns (uint256) {
        uint256 result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = (result * base) % modulus;
            }
            base = (base * base) % modulus;
            exponent /= 2;
        }
        return result;
    }
    
    function getRandomDiceRoll(uint256 seed) internal view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(seed, block.prevrandao))) % 6 + 1;
    }
    
    function encrypt(uint256 publicKey, uint256 privateKey, uint256 message) internal pure returns (uint256) {
        uint256 r = uint256(keccak256(abi.encodePacked(publicKey, privateKey, block.prevrandao)));
        return mulmod(powMod(g, r, p), message, p);
    }
    
    function decrypt(uint256 privateKey, uint256 publicKey, uint256 ciphertext) internal pure returns (uint256) {
        uint256 s = powMod(publicKey, privateKey, p);
        return mulmod(ciphertext, inverse(s, p), p);
    }
    
    event GameStarted(uint256 ciphertext1, uint256 ciphertext2);
}
```

---

Best usecase for "ElGamal" is when you don't want to reveal data but need some mathemathic operations.\
In the logic the "ElGamal" is a "diffie hellman". read my article for Diffie-Hellman [here](https://github.com/mosi-arch/research/blob/main/CipherPunk/11-Diffie_Hellman.md) & EC-DH [here](https://github.com/mosi-arch/research/blob/main/CipherPunk/07-EC-DH.md)

> my data is too old, please use your research
