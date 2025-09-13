from time import sleep
import os

encode_list = {
    'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..', '.' : '.-.-.-', ',' : '--..--', '?' : '..--..', '/' : '-..-.', '@' : '.--.-.', '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.', '0' : '-----', ' ' : '/', '!' : '-.-.--', '&' : '.-...', '=' : '-...-', '+' : '.-.-.', }

char_list = []
for char in encode_list:
    char_list.append(char)

decode_list = {}
for char in encode_list:
    code = encode_list[char]
    decode_list[code] = char

def print_codes(choose_list):
    columns = 11
    header_offset = 72
    code_pairs = list(choose_list.items())
    if choose_list == decode_list:
        print('\n' + ' ' * header_offset  +   '=================\n' + ' ' * header_offset + '|| Decode Mode ||\n' + ' ' * header_offset + '=================\n|' + f' Morse  = Char |' * columns)
    else:
        print('\n' + ' ' * header_offset  +   '=================\n' + ' ' * header_offset + '|| Encode Mode ||\n' + ' ' * header_offset + '=================\n|' + f' Morse  = Char |' * columns)
        print('\n|' + f' Char =  Morse |' * columns)
    print('|' + '---------------|' * columns)
    for i in range(0, len(code_pairs), columns):
        group = code_pairs[i:i+columns]
        print_list = ""
        for key, value in group:
            if choose_list == decode_list:
                print_list += f" {key:^7}=  {value:^3} |"
            else:
                print_list += f" {key:^3}  = {value:^7}|"
        print(f'|{print_list}')
        if i < len(code_pairs) - columns:
            print('|' + '               |' * columns)

def morse():
    print_codes(encode_list)
    message = input('\nEnter your message: ').upper()
    for char in message:
        if char not in char_list:
            print(f'\nYour message ({message}) contains characters  not in our morse database')
    code = ""
    for a in message:
        if a in encode_list:
            code += f'{ encode_list[a] } '
        if a not in encode_list:
            print(f"It seems like we're missing '{a}' from our database! How embarrassing... :(")
    print(f'{code}')
    return

def decode():
    while True:
        allowed = ['.', '-', '/', ' ']
        print_codes(decode_list)
        message = input('\nEnter your code with forward slash separators between words (.- .- / .- .-): ')
        for char in message:
            if char not in allowed:
                print(f'Your message to decode ({message}) contains incorrect symbols')
                break
            else:
                decoded_message = ""
                missing_code = []
                split = message.strip('/').split()
                # print(split)
                for code in split:
                    if code in decode_list:
                        decoded_message += f'{ decode_list[code]}'
                    else:
                        missing_code.append(code)
                if missing_code:
                    print(f"\n'{missing_code}' is missing from the code list")
                    break
                else:
                    print(f'{ decoded_message }')
                return

def choose():
    choice = input('\nDo you want to Decode or Encode? (D / E): ').upper()
    if choice != 'D' and choice != 'E':
        print(f"\n'{choice}' is not a valid entry. Please try again")
    elif choice == 'D':
        decode()
    else:
        morse()


while True:
    choose()
    end_prompt = input("\nShould we stop? (Y / N): ").upper()
    while end_prompt not in ['Y', 'N']:
        print( f"\nSorry, '{end_prompt}' is not a recognized command.", end='')
        end_prompt = input(f'\n\nPlease choose Y or N: ').upper()
    if end_prompt == 'Y':
        print("\nAdios!", end='')
        sleep(2)
        os.system('cls'if os.name == 'nt' else 'clear')
        break
    elif end_prompt == 'N':
        continue
    

