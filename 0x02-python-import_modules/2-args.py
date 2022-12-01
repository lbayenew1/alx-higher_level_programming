#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("1 argument:")
        print(f"{len(sys.argv) - 1}: {sys.argv[1]}")
    else:
        pos = len(sys.argv) - 1
        print(f"{pos} arguments:")
        for i in range(1, pos + 1):
            print(f"{i}: {sys.argv[i]}")
