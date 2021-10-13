letters = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
           'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
           'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
           'S': '...',
           'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '0': '-----',
           '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
           '8': '---..',
           '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
           '(': '-.--.',
           ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
           '_': '..--.-',
           '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '¿': '..-.-', '¡': '--...-'
           }

text_blank = input('Enter Text You Wanted To Convert: ')
text_blank = text_blank.upper()
to_convert = text_blank.split()

morse_text = []
print(to_convert)
for text in to_convert:
    for t in text:
        code = letters[t]
        morse_text.append(code)
        morse_text.append(' ')
    morse_text.append('/')
    morse_text.append(' ')
output = ''
for text in morse_text:
    output = output + text

print(output)
