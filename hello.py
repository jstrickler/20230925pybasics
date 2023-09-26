import sys
if len(sys.argv) <= 1:
    print("please provide an argument")
    exit()

print("Hello, Python world")

print(f"sys.argv: {sys.argv}")
print()
print(f"sys.argv[0]: {sys.argv[0]}")
print(f"sys.argv[1]: {sys.argv[1]}")

print(f"len(sys.argv): {len(sys.argv)}")
