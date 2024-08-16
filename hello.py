import sys

if len(sys.argv) > 1:
    version = sys.argv[1]
else:
    version = "default_version"

print(f"Running script with version: {version}")
