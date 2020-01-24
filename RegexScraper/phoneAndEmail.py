import re, pyperclip

phoneRegex = re.compile(r''' 
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional) 
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # next 4 digits
(((ext(\.)?\s) | x)         # extension (word) 
(\d{2,5}))?                 # extension (number)
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
# some._+thing@some._+thing.com

[a-zA-Z0-9_.+]+             # name (one or more)
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain

''', re.VERBOSE)

text = pyperclip.paste()
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])  # covers entire matched text

# TODO: Copy extracted data to clipboard

