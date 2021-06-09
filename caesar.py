import sys
import string
from random import randrange


def main():
    menu()
def menu():
    text = input("message: ")
    shift = int(input("shift: "))
    choice = input("option: ")
    if choice=="encode":
        encrypt = ""
        print(text)
        for i in text:
            if i.isalpha():
                alphabet = ord(i) + shift
                if alphabet <= ord("z"):
                    pass
                else:
                    alphabet -= 26
                newtext = chr(alphabet)
                encrypt += newtext
        print(encrypt)
        menu()
    elif choice=="decode":
        decrypt = ""
        print(text)
        for j in text:
            if j.isalpha():
                alphabet = ord(j) - shift
                if alphabet < ord("Z"):
                    alphabet += 26
            newtext_2 = chr(alphabet)
            decrypt += newtext_2
        print(decrypt)
        menu()
    elif choice=="OTP encode":
        encrypt = ""
        print(text)
        length = len(text)
        pad = []
        for i in text:
            if i.isalpha():
                random = randrange(10)
                alphabet = ord(i) + random
                pad.append(random)
                if alphabet <= ord("z"):
                    pass
                else:
                    alphabet -= 26
                newtext = chr(alphabet)
                encrypt += newtext
        print(encrypt)
        print(pad)
        menu()
    elif choice=="OTP decode":
        decrypt = ""
        print(text)
        for j in text:
            secret = int(input("Secret Key: "))
            if j.isalpha():
                alphabet = ord(j) - secret
                if alphabet < ord("Z"):
                    alphabet += 26
            newtext_2 = chr(alphabet)
            decrypt += newtext_2
        print(decrypt)
        menu()
    elif choice=="quit":
        sys.exit
    elif choice=="hack":
        string_alphabet = string.ascii_lowercase
        for character in range(26):
            translated = ''
            for symbol in text:
                if symbol not in string_alphabet:
                    translated += symbol
                else:
                    num = string_alphabet.find(symbol)
                    num -= character
                    if num < 0:
                        num += len(string_alphabet)
                    translated = "{0}{1}".format(translated,string_alphabet[num])
            print('Guess #{}: {}'.format(character,translated))
    else:
        print("Select Appropriate Action")
        menu()
main()
# add comments
