import logging

logging.basicConfig(
    filename="wombat.log",
    level=logging.INFO,
)

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# .debug(msg) .info(msg) .warning(msg) .error(msg)  .critical(msg)

logger.info("Starting program")

file_path = "DATA/margaret.txt"

try:
    with open(file_path) as file_in:
        pass
except FileNotFoundError as err:
    logger.warning(err)

with open('DATA/breakfast.txt') as breakfast_in:
    breakfast_items = breakfast_in.read().splitlines()

try:
    print(f"breakfast_items[99]: {breakfast_items[99]}\n")
except (IndexError, KeyError) as err:
    print(err)
except OSError as err:
    print(err)
except Exception as err:
    print(err)

nums = [800, 80, 1000, 0, 32, -4, 255, -8, 0, 400, 5, 5000]

for num in nums:
    try:
        result = 5000 / num  # code to test
    except ZeroDivisionError as err:
        print(err)   # error handlingn code
    else:
        print(f"{num:4d} {result:9.2f}")   # normal code








print("ALL DONE")