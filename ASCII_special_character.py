print("ASCII values of special characters:")
for char in range(33, 127):
    if not ('A' <= chr(char) <= 'Z' or 'a' <= chr(char) <= 'z' or '0' <= chr(char) <= '9'):
        print(f"{chr(char)}: {char}")
