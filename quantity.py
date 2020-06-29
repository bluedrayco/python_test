from sys import argv

def humanSize(bytes_value: int):
    divided_by = 1000
    sizes = [
        "KB",
        "MB",
        "GB",
        "TB",
        "PB",
        "EB",
        "ZB",
        "YB"
    ]
    pointer = 0
    result = bytes_value
    while(True):
        result = result/divided_by
        if result <divided_by or pointer==len(sizes)-1:
            break
        pointer+=1
    return f"{result:0.1f}{sizes[pointer]}"

if len(argv)<2:
    print (
"""
    The command need to be executed with one argument, example:
    python quantity.py 546432423423
""")
    exit(1)
if not argv[1].isnumeric():
    print("the parameter must be numeric")
    exit(1)

value = float(argv[1])

print(humanSize(value))

