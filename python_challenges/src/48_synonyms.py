'''Create a program that replaces specific words in a text file with their synonyms'''

def replace_words_in_file(file_path, replacements):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        for word, replacement in replacements.items():
            content = content.replace(word, replacement)

        with open(file_path, 'w') as file:
            file.write(content)

        print("Words replaced successfully!")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")

# Example usage
replacements = {"happy": "joyful", "sad": "melancholy"}
replace_words_in_file("example.txt", replacements)
