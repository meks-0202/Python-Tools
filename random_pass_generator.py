from random import choice
from sys import argv

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation


if __name__ == "__main__":
    print(argv)
    characters = ''

    if len(argv) > 1:
        
        pswd_length = int(argv[1])

        if '-l' in argv:
            characters += ascii_lowercase

        if '-L' in argv:
            characters += ascii_uppercase

        if '-p' in argv:
            characters += punctuation

        if '-d' in argv:
            characters += digits

        password = ''.join(choice(characters) for i in range(pswd_length))

        print(password)

    else:
        print("you didn\'t specify the length of your password\nexapmle command: python random_pass_generator.py [8] <-- integer")
	