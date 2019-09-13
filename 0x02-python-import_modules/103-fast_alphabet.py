#!/usr/bin/python3
uppercase = __import__("string").ascii_uppercase
__import__("os").write(1, bytes(uppercase + '\n', 'utf8'))
