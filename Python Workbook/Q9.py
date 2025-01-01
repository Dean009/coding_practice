#define a function that when called the function should return the more code equivalent of the input string
def string_to_morse_code(input_str: str) -> str:
    new_list = []
    morse_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", 
    "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", 
    "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", 
    "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", 
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", 
    "z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", 
    "9": "----.", "0": "-----",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", 
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", 
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", 
    "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.", 
    "$": "...-..-", "@": ".--.-.", " ": "/"}
    input_str = input_str.lower()

    for x in input_str:
        if x in morse_dict.keys():
            val = morse_dict[x]
            new_list.append(val)
    return " ".join(new_list) #return the list after making a new one joining on spaces, to remove ',' throughout the morse code
            
    
    
print(string_to_morse_code("HELLO WORLD!"))

