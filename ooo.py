import time
from datetime import datetime


def ooo(param1, param2):
    # ваш код
    print(f"{str(param1)} я {param2}")
    x = str(param1)
    print(f"Deutcshland -- mein herz in flamen {x}")
    print("Willst zu liebst du und verdamen")
    print("Deutcshland -- dein atem ist kalt")
    print("so jung und doch so alt!!!     !!")


def another_function(param):
    # какой-то другой код
    print(f"Another function: {param}")


if __name__ == "__main__":
    import sys

    function_name = sys.argv[1]
    if function_name == 'ooo':
        param1 = sys.argv[2]
        param2 = sys.argv[3]
        ooo(param1, param2)
    elif function_name == "another_function":
        another_function(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



