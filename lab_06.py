# To encode, we will turn var flat_password into a list, so we can iterate it.
# The iterating function will just add 3, with a check to make sure all numbers are single digit.
# Then, the list will be joined back together and turned into an integer for decoding purposes.
# We need to create several vars to use here: menu so we know where we are and one to hold the password, as well as
# a separate one to store the new encoded password.


def encode(flat_password):
    flassword = [int(x) for a, x in enumerate(str(flat_password))]
    pass_list = [x + 3 for x in flassword]
    pass_list = [x - 10 if x >= 10 else x for x in pass_list]
    encoded_password = ""
    for y in pass_list:
        encoded_password += str(y)
        int(encoded_password)
    return encoded_password

def decode(encode):
    flat_password = ""
    for y in pass_list:
        pass_list = [x + 10 if x>= 10 else x for x in pass_list]
        flat_password += str(y)
        int(flat_password)
    return flat_password



def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def main():
    user_menu = 0
    while user_menu != 3:
        menu()
        user_menu = int(input("Please enter an option: "))
        if user_menu == 1:
            global password
            password = int(input("Please enter your password to be encoded: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        if user_menu == 2:
            print(f"The encoded password is {encode}, and the original password is {decode(encode)}.")
            
            # This is purely for testing if the functions work, which they do.
            # WHat should actually be here is the decoder, which will be very easy to do.
            # It is essentially the encoder but backwards, which should be very easy to implement with the caveat that
            # we need to watch out for the special cases of 0, 1, and 2.
            print(encoded_password)
        if user_menu == 3:
            exit()
        if user_menu > 3 or user_menu < 1:
            print("Invalid Selection!")


if __name__ == '__main__':
    main()
