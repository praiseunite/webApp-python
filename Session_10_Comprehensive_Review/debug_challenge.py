# BUG HUNT: This program should read a file and print words starting with 'A' or 'a'.
# It has 5 bugs. Find them all!

import re

def analyze_text(filename)
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError
        print("File not found!")
        return
    
    # Regex to find words starting with A or a
    pattern = "\b[aA]\w*"
    words = re.findall(pattern content)
    
    print("Words starting with A:")
    for w in words:
        print(w)
        
    file.close()

# Note: You need a 'sample.txt' file in the same directory to test this.
# analyze_text("sample.txt")
