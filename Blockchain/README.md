
How Ancester CipherPunk's encrypt messages?\
Encrypt look like ceasar:
```py
# Python example
msg = input("message: ")

cipher ={
    "9": "q",
    "8": "w",
    "7": "e",
    "6": "r",
    "5": "t",
    "4": "y",
    "3": "u",
    "2": "i",
    "1": "o",
    "0": "p"
}

crypto = ""
for char in msg:
    crypto += cipher.get(char, "&") # + ""

print(f'0x{crypto}')
# input "10021363" - output '0xoppiouru'
# input "1020 3040 50 60" - output  '0xopip&upyp&tp&rp'
```

**Enjoy the encryption ERA...**

In this ERA you have to learn extra posible information for living safe.\
The first important thing before the encryption/decryption is: **Huffman Information Theroy**\
Example: `I(x) = log2(1/(P(x))) = -log2 P(x)`\
In this theory you must to know how much BIT's can transfer & translate.\
Following these names [huffman, shanon, neumann]
