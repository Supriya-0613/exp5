def is_palindrome(word):
    return word.lower().replace(" ", "") == word.lower().replace(" ", "")[::-1]

if __name__ == "__main__":
    word = input("Enter a word: ")
    print("Palindrome" if is_palindrome(word) else "Not Palindrome")