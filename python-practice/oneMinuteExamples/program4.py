# Remove Spaces From A String In Python

txt = """ this string
   contains   whitespaces
   """
# remove trailing whitespaces
print(txt.strip())

# remove all space characters
print(txt.replace(' ',''))

# remove all whitespaces (including tabs and newlines)
print(''.join(txt.split()))