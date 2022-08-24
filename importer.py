import os

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
                newValue = value.strip()[1:].replace("',", "").replace('",', '')

                data[newKey] = newValue

        print(data)
        exit()