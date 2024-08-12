# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

def morse_to_text(morse_code):
    # Splitting morse code into individual characters
    morse_words = morse_code.split('   ')
    decoded_message = ''
    
    for morse_word in morse_words:
        morse_chars = morse_word.split(' ')
        for char in morse_chars:
            decoded_message += MORSE_CODE_DICT.get(char, '')
        decoded_message += ' '
    
    return decoded_message.strip()

# Usage example
morse_input = '... --- ...'
print(morse_to_text(morse_input))
