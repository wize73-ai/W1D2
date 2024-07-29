from string_analyzer import analyze_string

def test_analyze_string():
    # Test case 1
    input_string = "Hello, World!"
    expected_output = {
        "num_characters": 13,
        "num_words": 2,
        "num_vowels": 3,
        "num_consonants": 7
    }
    assert analyze_string(input_string) == expected_output

    # Test case 2
    input_string = "Python is fun!"
    expected_output = {
        "num_characters": 14,
        "num_words": 3,
        "num_vowels": 3,
        "num_consonants": 8
    }
    assert analyze_string(input_string) == expected_output

    # Test case 3
    input_string = "12345"
    expected_output = {
        "num_characters": 5,
        "num_words": 1,
        "num_vowels": 0,
        "num_consonants": 0
    }
    assert analyze_string(input_string) == expected_output

    # Test case 4
    input_string = "Quick brown fox"
    expected_output = {
        "num_characters": 15,
        "num_words": 3,
        "num_vowels": 4,
        "num_consonants": 9
    }
    assert analyze_string(input_string) == expected_output

