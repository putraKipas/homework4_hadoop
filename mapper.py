#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    # Remove leading/trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Emit each word with a count of 1
    for word in words:
        print(f"{word}\t1")