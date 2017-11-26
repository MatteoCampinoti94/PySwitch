SWITCH_CASES = {
    1 : [
        'print("This is a makeshft switch statement")',
        'print("it can handle multiple instructions, including ones that need indentation")',
        'for i in range(1, 6):',
        '    print(i)',],
    'hello' : [
        'try:',
        '    with open("file.txt") as f:',
        '        print(f.readline())',
        'except FileNotFoundError:',
        '    print("File not found")'],
    'default' : ['print("This is the default case")']
    }

def switch(case):
    try:
        exec("\n".join(SWITCH_CASES.get(case, SWITCH_CASES['default'])))
    except KeyError:
        print("No default statement")

switch(1)

switch('hello')

switch('something')
