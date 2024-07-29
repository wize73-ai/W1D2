function analyzeString(inputString) {
    const numCharacters = inputString.length;
    const wordList = inputString.split(/\s+/); // Split by whitespace
    const numWords = wordList.length;

    // Cleaning the input: remove non-alphabetic characters and convert to lowercase
    const cleanedInput = inputString.replace(/[^a-zA-Z]/g, '').toLowerCase();

    const cleanLength = cleanedInput.length;

    // Counting vowels and consonants
    const vowels = 'aeiou';
    let numVowels = 0;
    for (let char of cleanedInput) {
        if (vowels.includes(char)) {
            numVowels++;
        }
    }
    const numConsonants = cleanLength - numVowels;

    const resultDict = {
        numCharacters: numCharacters,
        numWords: numWords,
        numVowels: numVowels,
        numConsonants: numConsonants
    };

    return resultDict;
}

const inputString = "Your sample input string goes here.";
console.log(analyzeString(inputString));
