def count(input_string):
    sentences = input_string.count('.') + input_string.count('!') + input_string.count('?')
    words = len(input_string.split())
    characters = len(input_string)
    return sentences, words, characters
input_text = input("Enter a string: ")
sentence_count, word_count, character_count = count(input_text)
print(f"\nNumber of sentences: {sentence_count}")
print(f"Number of words: {word_count}")
print(f"Number of characters: {character_count}")
