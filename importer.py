import os
import json

# Read all the files ordered by filename from folder importer with extension .php
for filename in sorted(os.listdir('importer')):
    if filename.endswith('.php'):
        # Read the file and group all the lines with the format 'key' => 'value'
        file = open(f'importer/{filename}')
        lines = file.readlines()
        file.close()
        data = {}
        for line in lines:
            if '=>' in line:
                key, value = line.split('=>')
                newKey = key.strip().replace("'", "").replace('"', '')

                # remove the first character from the value
                newValue = value.strip()[1:].replace("',", "").replace('",', '').replace("\\'", "'")

                data[newKey] = newValue

        jsonFile = filename.replace('.php', '.json')

        # transform data to a sorted json file at the json folder
        with open(f'json/{jsonFile}', 'w+') as outfile:
            json.dump(data, outfile, ensure_ascii=False, sort_keys=True, indent=4)
            outfile.close()
            print(f'json/{jsonFile}')
