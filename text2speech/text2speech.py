from gtts import gTTS
from io import BytesIO
import os
# import only system from os
from os import system, name
from datetime import datetime

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# # Clearing the Screen
# os.system('cls')

# # print out some text
# print('hello geeks\n'*10)
# 
# # sleep for 2 seconds after printing output
# sleep(2)
# 
# # now call function we defined above
# clear()

# Get user input
text = input("Enter text here: ")

# Map language input to gTTS parameters
language_map = {
    'en': ('en', 'us'),            # English (United States) - Default
    'es-mx': ('es', 'com.mx'),     # Spanish (Mexico)
    'en-au': ('en', 'com.au'),     # English (Australia)
    'en-uk': ('en', 'co.uk'),      # English (United Kingdom)
    'en-us': ('en', 'us'),         # English (United States)
    'en-ca': ('en', 'ca'),         # English (Canada)
    'en-in': ('en', 'co.in'),      # English (India)
    'en-ie': ('en', 'ie'),         # English (Ireland)
    'en-za': ('en', 'co.za'),      # English (South Africa)
    'en-ng': ('en', 'com.ng'),     # English (Nigeria)
    'fr': ('fr', 'fr'),            # French (France)
    'fr-ca': ('fr', 'ca'),         # French (Canada)
    'zh-CN': ('zh-CN', 'any'),     # Mandarin (China Mainland)
    'zh-TW': ('zh-TW', 'any'),     # Mandarin (Taiwan)
    'pt': ('pt', 'com.br'),        # Portuguese (Brazil) - Default
    'pt-br': ('pt', 'com.br'),     # Portuguese (Brazil)
    'pt-pt': ('pt', 'pt'),         # Portuguese (Portugal)
    'es': ('es', 'com.mx'),        # Spanish (Mexico) - Default
    'es-mx': ('es', 'com.mx'),     # Spanish (Mexico)
    'es-es': ('es', 'es'),         # Spanish (Spain)
    'es-us': ('es', 'us'),         # Spanish (United States)
    'de': ('de', 'de'),            # German (Germany)
    'it': ('it', 'it'),            # Italian (Italy)
    'ja': ('ja', 'jp'),            # Japanese (Japan)
    'ko': ('ko', 'kr'),            # Korean (South Korea)
    'ru': ('ru', 'ru'),            # Russian (Russia)
    'hi': ('hi', 'in'),            # Hindi (India)
    'ar': ('ar', 'sa'),            # Arabic (Saudi Arabia)
    'nl': ('nl', 'nl'),            # Dutch (Netherlands)
    'sv': ('sv', 'se'),            # Swedish (Sweden)
    'da': ('da', 'dk'),            # Danish (Denmark)
    'no': ('no', 'no'),            # Norwegian (Norway)
    'fi': ('fi', 'fi'),            # Finnish (Finland)
    'pl': ('pl', 'pl'),            # Polish (Poland)
    'cs': ('cs', 'cz'),            # Czech (Czech Republic)
    'hu': ('hu', 'hu'),            # Hungarian (Hungary)
    'tr': ('tr', 'tr'),            # Turkish (Turkey)
    'th': ('th', 'th'),            # Thai (Thailand)
    'vi': ('vi', 'vn'),            # Vietnamese (Vietnam)
    'id': ('id', 'id'),            # Indonesian (Indonesia)
    'ms': ('ms', 'my'),            # Malay (Malaysia)
    'tl': ('tl', 'ph'),            # Filipino (Philippines)
}

# Show languages availables
print("Language availables:")
for code in language_map.keys():
    print(f"{code}: {language_map[code][0]}")

# Choose language for text-to-speech
language = input("Enter language_code: ")

clear()

if language in language_map:
    lang, tld = language_map[language]

    # Create the BytesIO object
    mp3_fp = BytesIO()

    # Create the gTTS object
    tts = gTTS(text=text, lang=lang, tld=tld) if tld else gTTS(text=text, lang=lang)
    tts.write_to_fp(mp3_fp)

    # Obtain the current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")  # Formato: YYYYMMDD_HHMMSS
    
    # Save the BytesIO contents to a file (if needed)
    mp3_fp.seek(0)  # Move to the start of the BytesIO object
    filename = f"audio_{lang}.{tld}.{timestamp}.mp3"
    
    # Playing sound directly
    # from gtts import gTTS
    # from io import BytesIO
    #
    # mp3_fp = BytesIO()
    # tts = gTTS('hello', lang='en')
    # tts.write_to_fp(mp3_fp)
    # 
    # # Load `mp3_fp` as an mp3 file in
    # # the audio library of your choice

    with open(filename, 'wb') as f:
       f.write(mp3_fp.read())

    # In-Memory Handling: The BytesIO object allows you to store the audio data in memory. This can be advantageous when you want to avoid file I/O for performance reasons or when you're working in an environment where saving files is not practical.

    # Immediate Access: With BytesIO, you can process the audio directly after generating it—such as sending it over a network, playing it back on a web app, or processing it further—without having to handle file paths and disk space.

    # No Temporary Files: If you don’t need the audio file saved on disk (for example, in a web application where you're generating audio on-the-fly), using BytesIO prevents cluttering the file system with temporary files.
    
    # # Save audio file
    # filename = f"audio_{lang}.{tld}.{timestamp}.mp3" if tld else f"audio_{lang}.{timestamp}.mp3"
    # tts.save(filename)
    
    # Optional: Play the audio file using an external player
    # os.system("mpv output.mp3")

else:
    print("Invalid language choice.")
