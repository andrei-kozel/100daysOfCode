# Changing Case in a String with a Methods
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

# Adding Whitespace to String with Tabs Newlines
# \t - to add a Tab
# \n - to add a newline
print('Python')
print('\tPython')

favorite_language = ' python '
print(favorite_language)
print(favorite_language.strip())  # without whitespaces
#  To remove the whitespace from the string permanently,
# you have to store the stripped value back into the variable
favorite_language = favorite_language.strip()
print(favorite_language)  # without whitespaces
# rstrip - removes whitespaces from right side
# lstrip - removes whitespaces from left side
# strip - removes whitespaces from both sides
