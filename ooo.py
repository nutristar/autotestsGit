def ooo(param):
    # ваш код
    print(param)
    print("Deutcshland -- mein herz in flamen")

def another_function(param):
    # какой-то другой код
    print(f"Another function: {param}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        function_name = sys.argv[1]
        param = sys.argv[2]
        if function_name == "ooo":
            ooo(param)
        elif function_name == "another_function":
            another_function(param)




