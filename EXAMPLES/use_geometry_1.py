from alpha.mathlib import geometry  # find and load geometry.py  under alpha/mathlib
import sys

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)
print(f"geometry.PI: {geometry.PI}")
print()

# finding modules
#  1. current folder
#  2. folders in PYTHONPATH
#  3. predefined folders sys.prefix + "/lib"
for path in sys.path:
    print(path)

