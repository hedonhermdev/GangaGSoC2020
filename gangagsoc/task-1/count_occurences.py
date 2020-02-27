import re
import sys
import textract

# The filename of the pdf is passed as a command line argument.
filename = sys.argv[1]

count = 0

# Extract the text and convert it to lower case.
text_bytes = textract.process(filename)
text = text_bytes.decode("utf-8")
text = text.lower()

# Find all matches of the word "the" separated by a word boundary on both sides.
matches = re.findall(r"\bthe\b", text)

# Print the number of matches.
print(len(matches))
