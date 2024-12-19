'''Create a function to extract all URLs from a given text using regular expressions'''

import re

def extract_urls(text):
    url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9./?=_-]+'
    return re.findall(url_pattern, text)

# Example usage
text = "Visit https://www.example.com and http://example.org for more info."
urls = extract_urls(text)
print(f"Extracted URLs: {urls}")
