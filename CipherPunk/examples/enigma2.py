class Enigma:
    def __init__(self, rotor_order, rotor_positions, reflector):
        self.rotors = []
        for order, position in zip(rotor_order, rotor_positions):
            self.rotors.append(self.create_rotor(order, position))
        self.reflector = self.create_reflector(reflector)
    
    def create_rotor(self, order, position):
        rotor_wiring = {
            'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
            'IV': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
            'V': 'VZBRGITYUPSDNHLXAWMJQOFECK'
        }
        return Rotor(rotor_wiring[order], position)
    
    def create_reflector(self, reflector):
        reflector_wiring = {
            'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
            'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
        }
        return Reflector(reflector_wiring[reflector])
    
    def encrypt(self, message):
        ciphertext = ''
        for letter in message:
            if letter.isalpha():
                letter = letter.upper()
                for rotor in self.rotors[::-1]:
                    letter = rotor.forward(letter)
                letter = self.reflector.reflect(letter)
                for rotor in self.rotors:
                    letter = rotor.backward(letter)
                ciphertext += letter
                for rotor in self.rotors:
                    if rotor.rotate():
                        continue
                    else:
                        break
            else:
                ciphertext += letter
        return ciphertext


class Rotor:
    def __init__(self, wiring, position):
        self.wiring = wiring
        self.position = ord(position) - 65
        self.ring_setting = 0
    
    def forward(self, letter):
        input_num = ord(letter) - 65
        output_num = (input_num + self.position - self.ring_setting) % 26
        output_num = (ord(self.wiring[output_num]) - 65 - self.position + self.ring_setting) % 26
        output_letter = chr(output_num + 65)
        return output_letter
    
    def backward(self, letter):
        input_num = ord(letter) - 65
        output_num = (input_num + self.position - self.ring_setting) % 26
        for i, char in enumerate(self.wiring):
            if ord(char) - 65 == output_num:
                output_num = (i - self.position + self.ring_setting) % 26
                output_letter = chr(output_num + 65)
                return output_letter
    
    def rotate(self):
        self.position = (self.position + 1) % 26
        if self.position == 0:
            return True
        else:
            return False


class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring
    
    def reflect(self, letter):
        input_num = ord(letter) - 65
        output_num = ord(self.wiring[input_num]) - 65
        output_letter = chr(output_num + 65)
        return output_letter


rotor_order = ['III', 'II', 'I']
rotor_positions = []
for i in range(len(rotor_order)):
    position = input(f"Enter initial position of rotor {i+1} (A-Z): ")
    rotor_positions.append(position.upper())
reflector = 'B'
enigma = Enigma(rotor_order, rotor_positions, reflector)

message = input("Enter message to encrypt: ")
ciphertext = enigma.encrypt(message)
print("Ciphertext:", ciphertext)

enigma_decrypt = Enigma(rotor_order, rotor_positions, reflector)
decrypted_message = enigma_decrypt.encrypt(ciphertext)
print("Decrypted message:", decrypted_message)