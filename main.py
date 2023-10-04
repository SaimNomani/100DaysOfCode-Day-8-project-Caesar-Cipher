from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(message_technique, message, shift_amount):
    if (message_technique == 'encode') or (message_technique == 'decode'):
        converted_message = ""
        if message_technique == 'decode':
            shift_amount *= -1
        for n in range(0, len(message)):
            # To check if the character at the current index of the
            # message is in the alphabet list.
            if message[n] in alphabet:
                index = alphabet.index(message[n])
                converted_list_index = index + shift_amount
                # To handle the scenario when the new index exceeds 25.
                # This can also be addressed by duplicating the elements in the alphabet list.
                if converted_list_index > 25:
                    converted_list_index -= len(alphabet)
                converted_message += alphabet[converted_list_index]
            # If not, simply add that character to a new string without
            # changing its position in the original string.
            else:
                converted_message += message[n]
        print(f"the {message_technique}d message is: {converted_message}")
    else:
        print("Wrong request")


print(logo)
choice = 'yes'
while choice == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # to deal with very large shift numbers
    shift = shift % 26
    caesar(direction, text, shift)
    choice = (input("Type 'yes' if you want to go again, otherwise type 'no': ")).lower()
    if choice == 'no':
        print("Goodbye!!")
        break
