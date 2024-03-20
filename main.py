import requests
import xml.etree.ElementTree as ET

# The URL from which to fetch the XML data
url = 'https://community.grainfather.com/my-brews/data'

# Use requests to perform a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)
    
    # Now, you can navigate and read different parts of the XML tree
    # For example, to print out the tag and text of each child of the root:
    for child in root:
        print(child.tag, child.text)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
