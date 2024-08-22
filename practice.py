import requests
import os


url = 'https://www.jumia.com.ng/electronics/'
response = requests.get(url)
# Make a GET request
response = requests.get(url)

# Check if the response is in byte format
if isinstance(response.content, bytes):
    # Decode the byte response to a string
    text_data = response.content.decode('utf-8')  # or use the appropriate encoding
else:
    text_data = response.text  # If it's already a string, just use .text


# create a file with os
path = os.path.join(os.getcwd(), 'file.txt')

with open(path, 'w') as f:
    f.write(text_data)

with open(path, 'r') as r:
    r.readline()    





with open('j.json') as json_file:
    json.load(json_file)


with open('file.txt', 'r') as reference_file:
    with open ('file2.txt', 'a') as new_file:
        for line in reference_file:
            copy_file = new_file.write(line)
      