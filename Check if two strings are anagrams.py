#a word or phrase that is made by arranging the letters of another word or phrase in a different order.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
str1 = "listen"
str2 = "silent"
if are_anagrams(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
