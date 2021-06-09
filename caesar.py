import sys
import string
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
                Letter = chr(alphabet)
                encrypt += Letter
        print(encrypt)
        menu()
    elif choice=="decode":
        decrypt = ""
        print(text)
        for i1 in text:
            if i1.isalpha():
                alphabet = ord(i1) - shift
                if alphabet < ord("Z"):
                    alphabet += 26
            new = chr(alphabet)
            decrypt += new
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
