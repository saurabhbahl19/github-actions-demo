# hello.py (example)
import sys

version = sys.argv[1] if len(sys.argv) > 1 else "unknown"
with open('version.txt', 'w') as f:
    f.write(version)
