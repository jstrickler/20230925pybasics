FILE_NAME = "DATA/mary.txt"  # same on Windows, Mac, and Linux

mary_in = open(FILE_NAME, "r")
# ... read file here ...
mary_in.close()

# with EXPR as VAR:
with open(FILE_NAME, "r") as mary_in:
    # read file here...
    print(f"mary_in: {mary_in}")
print()

with open(FILE_NAME) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()   # trim all trailing whitespace from line
        print(line)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()  # read entire file (with embedded newlines)
    print("NORMAL CONTENTS:")
    print(contents)
    print("RAW CONTENTS")
    print(repr(contents))
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()
    all_lines_without_nl = contents.splitlines()
    print(all_lines_without_nl)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)



