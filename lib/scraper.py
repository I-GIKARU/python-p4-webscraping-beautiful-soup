from bs4 import BeautifulSoup
import requests

# Set headers to avoid 403 errors from the server
headers = {'user-agent': 'my-app/0.0.1'}

# Make the HTTP GET request
html = requests.get("https://flatironschool.com/", headers=headers)

# Parse the response HTML with BeautifulSoup
doc = BeautifulSoup(html.text, 'html.parser')

# Use CSS selector to extract a specific element (e.g., the homepage hero heading)
# NOTE: this class might change — always inspect element to confirm.
headline = doc.select('.heading-financier')

# Print the text content if found
if headline:
    print(headline[0].text.strip())
else:
    print("Headline not found.")
