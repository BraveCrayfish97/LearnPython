spanish_dict = {
    "hi": "Hola",
    "hello": "Hola",
    "bye": "Adios",
    "water": "Agua",
    "go": "Va",
    "i": 'Yo',
    "you": "Tu",
    "name": "Nombre",
    "year": "Año",
    "what": "Qué",
    "why": "Por qué",
    "becuase": "Porque",
    "where": "Dónde"
    }

while(True):
    try:
        engish_word = input("What word would you like to convert to spanish?\n> ")
        engish_word = engish_word.lower()
        bad_input = False
    
        spanish_word = spanish_dict[engish_word]
        print(f'\n"{engish_word.capitalize()}" means "{spanish_word}" in spanish.\n')
        
    except KeyError:
        print(f'I found no match for "{engish_word.capitalize()}" in this dictionary because I am a noob.')