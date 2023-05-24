def string_to_hex(string):
    hex_string = ''
    for char in string:
        hex_value = hex(ord(char))[2:]
        hex_string += hex_value.zfill(2)
    return hex_string

if __name__ == '__main__':
    string = 'Hello, World!'
    hex_string = string_to_hex(string)
    print(hex_string)

# =======================

