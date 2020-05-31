# In python 3 all strings are unicode.
# We can enter not-easily-typable unicode chars in a variety of ways 
print('Using unicode chars in python')
print('* Use slash-u followed by unicode number/code')
print('\t', '\\u0101 =>', '\u0101')
print('\t', 'S\\u0101dhakam =>', 'S\u0101dhakam')
print('\t', '\\u00bd =>', '\u00bd')
print('\t', 'or, \\xbd =>', '\xbd')
print()
print("* Use the charactor's name with \\N")
print('\t', "\\N{TAMIL FRACTION ONE QUARTER} =>", "\N{TAMIL FRACTION ONE QUARTER}")
print('\t', "\\N{VULGAR FRACTION ONE HALF} =>", "\N{VULGAR FRACTION ONE HALF}")

