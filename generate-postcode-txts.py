from urllib.request import urlopen
import csv
import os

file_path = "output/condensed_postcode_to_constituency_mapping.csv"

# Define the directory
directory = 'docs/postcodes'

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)
print('Directory created if not existing')

with open(file_path, 'r') as file:
    reader = csv.reader(file)

    # Skip the header
    next(reader)

    # For each line, get the postcode and the new_constituency_name
    i = 0
    for row in reader:
        postcode, new_constituency_name = row

        # Remove whitespace from the postcode to use it as a filename
        filename = postcode.replace(" ", "")

        # Create a new text file in the 'docs' directory with the filename as the postcode
        with open(os.path.join(directory, f'{filename}.txt'), 'w') as f:
            # Write the new_constituency_name to the text file
            f.write(new_constituency_name)
        
        i += 1
        if i % 100000 == 0:
            print(f'Processed {i} postcodes')
