

def decode_string(encoded_string):
    decoded_message = []
    i = 0
    while i < len(encoded_string):
        count = int(encoded_string[i])
        char = encoded_string[i + 1]
        decoded_message.append(char * count)
        i += 2
    return ''.join(decoded_message)


def main():
    print(decode_string(input().strip()))

if __name__ == "__main__":
    main()
