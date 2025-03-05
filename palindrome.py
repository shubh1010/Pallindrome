"""
Validates strings as palindromes.
"""

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

while True:
    user_input = input("Enter a word or phrase to check if it's a palindrome (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    result = is_palindrome(user_input)
    if not result:
        print("No, it's not a palindrome. Try again.")
    else:
        print(result)
