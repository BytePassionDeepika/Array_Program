def convert_case(input_string):
    result = ""
    for char in input_string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32) 
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32) 
        else:
            result += char  
    return result
input_text = input("Enter a string: ")
converted_text = convert_case(input_text)
print(f"\nConverted string: {converted_text}")
