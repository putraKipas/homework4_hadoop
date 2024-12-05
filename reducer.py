#!/usr/bin/env python3
import sys

current_word = None
current_total_count = 0
word = None

# Read input from stdin
for line in sys.stdin:
    # Remove leading/trailing whitespace
    line = line.strip()
    # Parse the input (word \t count)
    word, count = line.split("\t", 1)
    try:
        count = int(count)
    except ValueError:
        # Ignore lines with invalid count
        continue
    
    # If the word is the same as the previous one, increment the count
    if word == current_word:
        current_total_count += count
    else:
        # Otherwise, print the word and its count
        if current_word:
            print(f"{current_word}\t{current_total_count}")
        current_word = word
        current_total_count = count

# Output the last word's count
if current_word == word:
    print(f"{current_word}\t{current_total_count}")