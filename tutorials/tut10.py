import string

ALPHABET = string.ascii_lowercase


def write_file(filename, message):
    try:
        f_obj = open(filename, "w")
        f_obj.write(message)
        f_obj.close()
    except OSError as err:
        print("Could not write to " + filename + ", try again")
        print(err)


def encrypt(message, shift):
    result = ""
    for char in message.lower():
        if char in ALPHABET:
            index = ALPHABET.index(char) + shift
            result += ALPHABET[index % len(ALPHABET)]
        else:
            result += char

    return result


def create_test_file():
    success = False
    while not success:
        message = input("Enter the message to encrypt: ")
        shift = input("Enter an integer shift: ")
        try:
            shift = int(shift)
            encrypted = encrypt(message, shift)
            file_contents = f"{shift}\n{encrypted}"
            write_file("encrypted.txt", file_contents)
            print("Success!")
            success = True
        except Exception as e:
            print("Something went wrong, try again")
            print(e)


def decrypt_file(filename):
    # Try to open filename. Read the first line into an integer
    # representing the shift value, then decrypt the rest of the file
    # using the Caesar cipher with the lowercase alphabet.
    # Return the resulting text string.
    # If something fails, return None
    pass


def main():
    # call decrypt_file with the filename 'encrypted.txt'.
    # If decrypt_file returns None, return from main. Otherwise,
    # write the resulting message to a new file named 'decrypted.txt'
    pass


if __name__ == "__main__":
    # main()
    create_test_file()
