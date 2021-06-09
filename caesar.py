import sys
def main():
    menu()
def menu():
    text = input("message: ")
    shift = int(input("shift: "))
    choice = input("choice: ")
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
    elif choice == "decode":
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
    elif choice == "quit":
        sys.exit
    else:
        print("Select Appropriate Action")
        menu()
main()
