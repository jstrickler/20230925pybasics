import os

def say_hello():
    print("Hello, Python world")

result = say_hello()
print(f"result: {result}")

def get_message():
    return "Hello from the dark mysteries of Python"

m = get_message()
print(f"m: {m}")

def double(x):
    return 2 * x



print(f"double(5): {double(5)}")
print(f"double('abc'): {double('abc')}")

result = 5 + double(99)
print(f"result: {result}")


def greet(whom="world"):
    print(f"Hello, {whom}")

greet("Mom")
greet("New York")
greet()

def grep(search_term, *file_paths, show_name=False):
    for file_path in file_paths:
        short_name = os.path.basename(file_path)
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    if show_name:
                        print(f"{short_name}:", end=" ")
                    print(raw_line.rstrip())

grep("bird")
grep("bird", "DATA/parrot.txt", "DATA/alice.txt", show_name=True)








