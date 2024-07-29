def analyze_string(input_string):
    num_characters = len(input_string)
    word_list = input_string.split()
    num_words = len(word_list)
    
    # Cleaning the input: remove non-alphabetic characters and convert to lowercase
    cleaned_input = ''.join(char.lower() for char in input_string if char.isalpha())
    
    clean_length = len(cleaned_input)
    
    # Counting vowels and consonants
    vowels = "aeiou"
    num_vowels = sum(1 for char in cleaned_input if char in vowels)
    num_consonants = clean_length - num_vowels

    result_dict = {
        "num_characters": num_characters,
        "num_words": num_words,
        "num_vowels": num_vowels,
        "num_consonants": num_consonants
    }
    
    return result_dict

if __name__ == "__main__":
    input_string = "Your sample input string goes here."
    print(analyze_string(input_string))

