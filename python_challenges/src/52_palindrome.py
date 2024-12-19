'''Create a program that checks if a string is a palindrome'''

def is_palindrome(s):
    # This line filters out any characters from the string s that are not alphanumeric (i.e., not letters or numbers).
    # The str.isalnum method returns True for alphanumeric characters and False for others, such as spaces or punctuation marks.
    # The filter() function applies this method to each character in the string s, effectively removing non-alphanumeric characters.
    cleaned_str = ''.join(filter(str.isalnum, s)).lower()  # Remove non-alphanumeric and convert to lowercase
    return cleaned_str == cleaned_str[::-1]

# Example usage
input_string = "A man, a plan, a canal, Panama"
print(f"Is the string a palindrome? {is_palindrome(input_string)}")
