def is_palindrome(word):
    return word == word[::-1]

def print_palindrome_words(sentence):
    words = sentence.split()
    palindrome_words = [word for word in words if is_palindrome(word)]
    
    if palindrome_words:
        print("Palindrome words in the given sentence:")
        for palindrome_word in palindrome_words:
            print(palindrome_word)
    else:
        print("No palindrome words found in the given sentence.")

# Example usage:
sentence = input("Enter The Sentence:")
print_palindrome_words(sentence)
