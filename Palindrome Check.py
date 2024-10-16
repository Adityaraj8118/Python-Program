s = input("Enter a string: ").lower().replace(" ", "")
print("Palindrome" if s == s[::-1] else "Not a palindrome")
