
animal = "wombat"   # global name (file-global)

def spam():
    x = 100  # local name
    def ham():
        print(x)
    animal = "pine marten"
    print("Hello from spam()")
    print(f"x: {x}")


spam()
# print(f"x: {x}")  INVALID
print(f"animal: {animal}")

