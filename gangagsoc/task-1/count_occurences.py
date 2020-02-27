import re
import sys
import textract

# The filename of the pdf is passed as a command line argument.

def extract_text(pdf_file_name):
    text_bytes = textract.process(filename)
    text = text_bytes.decode("utf-8")
    return text

def num_occurences(word, text):
    text = text.lower()
    matches = re.findall(rf"\b{word}\b", text)
    return len(matches)


if __name__ == '__main__':
    filename = sys.argv[1]
    word = 'the'
    text = extract_text(filename)
    num_occurences = find_occurences(word, text)
    print(num_occurences)
