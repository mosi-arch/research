def hex_to_string(hex_string):
    string = ''
    for i in range(0, len(hex_string), 2):
        hex_value = hex_string[i:i+2]
        string += chr(int(hex_value, 16))
    return string

if __name__ == '__main__':
    hex_string = '48656c6c6f2c20576f726c6421'
    string = hex_to_string(hex_string)
    print(string)