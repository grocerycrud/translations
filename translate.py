import json
import os

# Everything is based on the english.json file
# For example if there is a key missing in English then we are also removing it from all the other languages
# If we have added a new key then we are adding it to all the other languages as well
englishFile = open('json/English.json')
englishData = json.load(englishFile)
englishFile.close()

# create a folder with name php if it doesn't exist
if not os.path.exists('php'):
    os.makedirs('php')

def jsonToPhp(jsonData, language):
    phpFile = open('php/' + language + '.php', 'w')
    phpFile.write('<?php\n\n')
    phpFile.write('return [\n')
    # sort by key jsonData
    for key in sorted(jsonData):
        phpFile.write('    \'' + key + '\' => \'' + jsonData[key].replace("'", "\\'") + '\',\n')
    phpFile.write('];\n')
    phpFile.close()

jsonToPhp(englishData, 'English')

# Read all the folder within the folder json with extension .json
for filename in os.listdir('json'):
    if filename.endswith('.json'):
        # Open the file and read the englishData
        file = open(f'json/{filename}')
        languageData = json.load(file)

        # Loop through the englishData and check if the key is missing in the languageData
        for key, value in englishData.items():
            if key not in languageData:
                languageData[key] = value

        file.close()

        # Write the languageData to the filename and remove the filename extension
        jsonToPhp(languageData, filename.replace('.json', ''))