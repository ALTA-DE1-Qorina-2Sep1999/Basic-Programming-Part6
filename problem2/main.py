def caesar(offset, input_str):
    result = ""
 
    for i in range(len(input_str)):
        char = input_str[i]
        if (char.isupper()):
            result += chr((ord(char) + offset-65) % 26 + 65)
        else:
            result += chr((ord(char) + offset-97) % 26 + 97)
    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl