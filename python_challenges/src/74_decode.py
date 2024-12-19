# You are given a Google Doc like this one that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.
# The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.
# The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.
# Any positions in the grid that do not have a specified character should be filled with a space character.
# You can assume the document will always have the same format as the example document linked above.
# For example, the simplified example document linked above draws out the letter 'F':

# █▀▀▀
# █▀▀ 
# █   
# Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

# Specifications
# Your code must be written in Python (preferred) or JavaScript.
# You may use external libraries.
# You may write helper functions, but there should be one function that:
# 1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND
# 2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters. 

import requests
from bs4 import BeautifulSoup

def fetch_document(url):
    """Fetches the content of the Google Doc."""
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully got the document.")
        # print(response.text[:500])
        return response.text
    else:
        print(f"Error fetching document: {response.status_code}")
        return ""

def parse_coordinates_from_html(doc_content):
    """Parses the document content and returns a list of (x, y, char) tuples."""
    soup = BeautifulSoup(doc_content, 'html.parser')
    
    # Find the table with the class "c8" (may vary depending on the doc structure)
    table = soup.find('table')
    
    if not table:
        print("No table found.")
        return []
    
     # Print the table for inspection
    print("Table found:")
    # print(table.prettify()) 
    
    rows = table.find_all('tr')
    coordinates = []

    for row in rows:
        # Extract all columns (td) from each row
        cols = row.find_all('td')
        
        # Ensure the row has exactly three columns
        if len(cols) == 3:
            try:
                # Extract values from the <span> inside each <td> (text content)
                x = int(cols[0].find('span').text.strip())  # First column (x coordinate)
                char = cols[1].find('span').text.strip()   # Second column (character)
                y = int(cols[2].find('span').text.strip())  # Third column (y coordinate)
                
                coordinates.append((x, y, char))
            except (ValueError, AttributeError) as e:
                # Skip rows that cannot be parsed correctly and print error
                print(f"Skipping row due to error: {row} (Error: {e})")
                continue
        else:
            print(f"Skipping row with invalid number of columns: {row}")

    return coordinates

def get_grid_dimensions(coordinates):
    """Returns the dimensions of the grid (max_x, max_y)."""
    if coordinates:
        max_x = max(x for x, _, _ in coordinates)
        max_y = max(y for _, y, _ in coordinates)
        return max_x, max_y
    return 0, 0

def create_empty_grid(max_x, max_y):
    """Creates an empty grid filled with spaces."""
    return [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

def fill_grid(grid, coordinates):
    """Fills the grid with characters based on coordinates."""
    for x, y, char in coordinates:
        grid[y][x] = char

def print_grid(grid):
    """Prints the grid."""
    for row in grid:
        print(''.join(row))

def create_grid_from_google_doc(url):
    """Main function to fetch, parse, and print the grid."""
    doc_content = fetch_document(url)
    if not doc_content:
        return

    coordinates = parse_coordinates_from_html(doc_content)
    if not coordinates:
        print("No coordinates found in the document.")
        return
    
    max_x, max_y = get_grid_dimensions(coordinates)
    if max_x == 0 or max_y == 0:
        print("Invalid grid dimensions.")
        return
    
    grid = create_empty_grid(max_x, max_y)
    fill_grid(grid, coordinates)
    print_grid(grid)


# URL to use:
url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
create_grid_from_google_doc(url)
