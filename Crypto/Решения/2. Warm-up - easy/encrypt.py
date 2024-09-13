
key = b'tired_of_such_tasks'

def main():
    with open("flag.jpg", "rb") as file:
        text = file.read()
    ct = bytes([text[i] ^ key[i % len(key)] for i in range(len(text))])
    with open("cipher.jpg", "wb") as file:
        file.write(ct)  

if __name__ == "__main__":
    main()
