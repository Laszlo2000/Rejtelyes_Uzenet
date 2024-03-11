def decode(message: str):
    uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '\n', '!', ':']
    lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '\n', '!', ':']
    secret_uppercase_list = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                             'U',
                             'V', 'W', 'X', 'Y', 'Z', 'A', 'B', ' ', '\n', '!', ':']
    secret_lowercase_list = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                             'u',
                             'v', 'w', 'x', 'y', 'z', 'a', 'b', ' ', '\n', '!', ':']
    decoded_message = ""
    for i in range(len(message)):

        if message[i] in uppercase_list:
            index_ULS = uppercase_list.index(message[i])
            decoded_message += secret_uppercase_list[index_ULS]

        elif message[i] in lowercase_list:
            index_LLS = lowercase_list.index(message[i])
            decoded_message += secret_lowercase_list[index_LLS]

    return decoded_message


if __name__ == '__main__':
    message = '''
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb
    '''
    print(decode(message))